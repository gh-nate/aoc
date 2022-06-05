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
    instructions = f.readlines()

width = 1000
height = 1000

lights_1 = [[False for _ in range(width)] for _ in range(height)]
lights_2 = [[0 for _ in range(width)] for _ in range(height)]

turn_on = re.compile('turn on (\d+),(\d+) through (\d+),(\d+)')
turn_off = re.compile('turn off (\d+),(\d+) through (\d+),(\d+)')
toggle = re.compile('toggle (\d+),(\d+) through (\d+),(\d+)')


def indices(groups):
    start_x, start_y, end_x, end_y = groups
    for y in range(int(start_y), int(end_y) + 1):
        for x in range(int(start_x), int(end_x) + 1):
            yield y, x


for instruction in instructions:
    if m := turn_on.match(instruction):
        for y, x in indices(m.groups()):
            lights_1[y][x] = True
            lights_2[y][x] += 1
    elif m := turn_off.match(instruction):
        for y, x in indices(m.groups()):
            lights_1[y][x] = False
            if lights_2[y][x] > 0:
                lights_2[y][x] -= 1
    elif m := toggle.match(instruction):
        for y, x in indices(m.groups()):
            lights_1[y][x] = not lights_1[y][x]
            lights_2[y][x] += 2

number_of_lights_lit = 0
total_brightness = 0
for row_1, row_2 in zip(lights_1, lights_2):
    number_of_lights_lit += row_1.count(True)
    total_brightness += sum(row_2)

print(f'Part 1: {number_of_lights_lit}')
print(f'Part 2: {total_brightness}')
