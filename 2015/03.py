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
    directions = f.read()

position = (0, 0)

visited_1 = set()
visited_1.add(position)

santa = (0, 0)
robot = (0, 0)

visited_2 = set()
visited_2.add(santa)

for index, direction in enumerate(directions):
    is_even = index % 2 == 0
    match direction:
        case '>':
            position = (position[0] + 1, position[1])
            if is_even:
                santa = (santa[0] + 1, santa[1])
            else:
                robot = (robot[0] + 1, robot[1])
        case '<':
            position = (position[0] - 1, position[1])
            if is_even:
                santa = (santa[0] - 1, santa[1])
            else:
                robot = (robot[0] - 1, robot[1])
        case '^':
            position = (position[0], position[1] + 1)
            if is_even:
                santa = (santa[0], santa[1] + 1)
            else:
                robot = (robot[0], robot[1] + 1)
        case 'v':
            position = (position[0], position[1] - 1)
            if is_even:
                santa = (santa[0], santa[1] - 1)
            else:
                robot = (robot[0], robot[1] - 1)
    visited_1.add(position)
    if is_even:
        visited_2.add(santa)
    else:
        visited_2.add(robot)

print(f'Part 1: {len(visited_1)}')
print(f'Part 2: {len(visited_2)}')
