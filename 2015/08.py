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

with open('input') as f:
    strings = [s.rstrip() for s in f]


def calculate_part_1(s):
    len_lit = len(s)
    len_mem = 0
    i = 1
    while i < len_lit - 1:  # ignore opening and closing double quotes
        if s[i] == '\\':
            match s[i + 1]:
                case '\\' | '"':
                    i += 1
                case 'x':
                    i += 3
        len_mem += 1
        i += 1
    return len_lit - len_mem


def calculate_part_2(s):
    len_lit = len(s)
    len_mem = 6  # opening and closing double quotes counted
    i = 1
    while i < len_lit - 1:  # ignore opening and closing double quotes
        match s[i]:
            case '\\' | '"':
                len_mem += 1
        len_mem += 1
        i += 1
    return len_mem - len_lit


total_part_1 = 0
total_part_2 = 0
for string in strings:
    total_part_1 += calculate_part_1(string)
    total_part_2 += calculate_part_2(string)

print(f'Part 1: {total_part_1}')
print(f'Part 2: {total_part_2}')
