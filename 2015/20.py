# Copyright (c) 2022 gh-nate
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import itertools

puzzle_input = int(input('Please enter your puzzle input: ').rstrip())


def factors(x):
    i = 1
    while i * i <= x:
        if x % i == 0:
            yield i
            div = x // i
            if div != i:
                yield div
        i += 1


for house in itertools.count(1):
    if sum(elf * 10 for elf in factors(house)) >= puzzle_input:
        break

print(f'Part 1: {house}')

elves_work_history = {}
for house in itertools.count(1):
    presents = 0
    for elf in factors(house):
        if elf in elves_work_history and elves_work_history[elf] == 50:
            continue
        presents += elf * 11
        elves_work_history.setdefault(elf, 0)
        elves_work_history[elf] += 1
    if presents >= puzzle_input:
        break

print(f'Part 2: {house}')
