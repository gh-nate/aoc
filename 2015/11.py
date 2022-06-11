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
import string

puzzle_input = input('Please enter your puzzle input: ')

len_alphabets = len(string.ascii_lowercase)
alphabets_index = dict(zip(string.ascii_lowercase, range(len_alphabets)))


def increment(s):
    i = len(s) - 1
    while True:
        pos = alphabets_index[s[i]] + 1
        has_wraparound = pos == len_alphabets
        if has_wraparound and i == 0:
            break
        pos %= len_alphabets
        s = s[:i] + string.ascii_lowercase[pos] + s[i + 1 :]
        if not has_wraparound:
            break
        i -= 1
    return s


def meets_requirement_1(s):
    for i in range(len(s) - 2):
        if (
            alphabets_index[s[i]]
            == alphabets_index[s[i + 1]] - 1
            == alphabets_index[s[i + 2]] - 2
        ):
            return True
    return False


def meets_requirement_2(s):
    for c in s:
        match c:
            case 'i' | 'o' | 'l':
                return False
    return True


def meets_requirement_3(s):
    nop = set()
    for t in itertools.pairwise(s):
        if t[0] == t[1]:
            nop.add(t)
    return len(nop) >= 2


def meets_requirements(s):
    return meets_requirement_1(s) and meets_requirement_2(s) and meets_requirement_3(s)


def generate(s):
    while True:
        s = increment(s)
        if meets_requirements(s):
            return s


new_password = generate(puzzle_input)

print(f'Part 1: {new_password}')
print(f'Part 2: {generate(new_password)}')
