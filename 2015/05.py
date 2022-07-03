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


def is_nice_1(s):
    number_of_vowels = 0
    p = ''  # previous character
    has_pair = False
    for c in s:
        match c:
            case 'a' | 'e' | 'i' | 'o' | 'u':
                number_of_vowels += 1
        if not has_pair and p == c:
            has_pair = True
        match f'{p}{c}':
            case 'ab' | 'cd' | 'pq' | 'xy':
                return False
        p = c
    return number_of_vowels >= 3 and has_pair


def is_nice_2(s):
    has_non_overlapping_pairs = False
    has_sandwich = False
    pairs_indices = {}
    double_limit = len(s) - 1
    triple_limit = double_limit - 1
    for i in range(double_limit):
        if not has_non_overlapping_pairs:
            substr = s[i : i + 2]
            if substr in pairs_indices:
                if pairs_indices[substr] != i:
                    has_non_overlapping_pairs = True
            else:
                pairs_indices[substr] = i + 1
        if not has_sandwich and i < triple_limit:
            substr = s[i : i + 3]
            if substr[0] == substr[2]:
                has_sandwich = True
    return has_non_overlapping_pairs and has_sandwich


count_1 = 0
count_2 = 0
for string in strings:
    if is_nice_1(string):
        count_1 += 1
    if is_nice_2(string):
        count_2 += 1

print(f'Part 1: {count_1}')
print(f'Part 2: {count_2}')
