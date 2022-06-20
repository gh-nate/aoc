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

import sys

with open('input') as f:
    capacities = [int(l.rstrip()) for l in f]


length_shortest_branches = sys.maxsize
max_capacity = 150
number_of_combinations = 0
number_of_ways = 0


def find_combinations(containers, branch):
    total_capacity = sum(branch)
    if total_capacity < max_capacity:
        for i, c in enumerate(containers):
            find_combinations(containers[i + 1 :], branch + [c])
    elif total_capacity == max_capacity:
        global length_shortest_branches, number_of_combinations, number_of_ways
        length_branch = len(branch)
        if length_branch < length_shortest_branches:
            length_shortest_branches = length_branch
            number_of_ways = 1
        elif length_branch == length_shortest_branches:
            number_of_ways += 1
        number_of_combinations += 1


find_combinations(capacities, [])

print(f'Part 1: {number_of_combinations}')
print(f'Part 2: {number_of_ways}')
