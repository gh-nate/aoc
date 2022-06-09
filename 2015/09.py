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
import re
import sys

with open('input') as f:
    lines = f.readlines()

distances = {}
locations = set()
o = re.compile('(\w+) to (\w+) = (\d+)')

for line in lines:
    if m := o.match(line):
        location_1, location_2, distance = m.groups()
        distances[(location_1, location_2)] = distances[(location_2, location_1)] = int(
            distance
        )
        locations.add(location_1)
        locations.add(location_2)

shortest_distance = sys.maxsize
longest_distance = 0
for p in itertools.permutations(locations):
    distance = sum(distances[t] for t in itertools.pairwise(p))
    if distance < shortest_distance:
        shortest_distance = distance
    if distance > longest_distance:
        longest_distance = distance

print(f'Part 1: {shortest_distance}')
print(f'Part 2: {longest_distance}')
