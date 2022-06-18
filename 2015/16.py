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

import re

with open('input') as f:
    descriptions = f.readlines()

max_score_1 = 0
max_score_2 = 0
pattern = 'Sue (\d+): '
things = {
    'children': '3',
    'cats': '7',
    'samoyeds': '2',
    'pomeranians': '3',
    'akitas': '0',
    'vizslas': '0',
    'goldfish': '5',
    'trees': '3',
    'cars': '2',
    'perfumes': '1',
}
number_of_things = len(things)

for _ in range(3):
    for index, thing in enumerate(things.keys()):
        if index == 0:
            pattern += '('
        elif index < number_of_things:
            pattern += '|'
        pattern += f'{thing}'
    pattern += '): (\d+), '

o = re.compile(pattern[:-2])


def check2(property, count):
    match property:
        case 'cats' | 'trees' if things[property] < count:
            return True
        case 'pomeranians' | 'goldfish' if things[property] > count:
            return True
        case _ if things[property] == count:
            return True
    return False


for description in descriptions:
    score_1 = 0
    score_2 = 0
    if m := o.match(description):
        sue, p_1, c_1, p_2, c_2, p_3, c_3 = m.groups()
        if things[p_1] == c_1:
            score_1 += 1
        if check2(p_1, c_1):
            score_2 += 1
        if things[p_2] == c_2:
            score_1 += 1
        if check2(p_2, c_2):
            score_2 += 1
        if things[p_3] == c_3:
            score_1 += 1
        if check2(p_3, c_3):
            score_2 += 1
        if score_1 > max_score_1:
            max_score_1 = score_1
            sue_number_1 = sue
        if score_2 > max_score_2:
            max_score_2 = score_2
            sue_number_2 = sue

print(f'Part 1: {sue_number_1}')
print(f'Part 2: {sue_number_2}')
