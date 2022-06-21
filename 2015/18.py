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

import copy

dimension = 100
filename = 'input'
off_char = '.'
on_char = '#'

corner_coordinates = [
    (0, 0),
    (0, dimension - 1),
    (dimension - 1, dimension - 1),
    (dimension - 1, 0),
]
relative_neighbor_coordinates = [
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
]


def animate(skip_corners):
    global grid
    for _ in range(100):  # steps
        grid_copy = copy.deepcopy(grid)
        for y, x in ((y, x) for y in range(dimension) for x in range(dimension)):
            if skip_corners and (y, x) in corner_coordinates:
                continue
            number_of_neighbors_that_are_on = 0
            for i, j in relative_neighbor_coordinates:
                i += x
                j += y
                if 0 <= i < dimension and 0 <= j < dimension and grid[j][i] == on_char:
                    number_of_neighbors_that_are_on += 1
            if grid[y][x] == on_char:
                if (
                    number_of_neighbors_that_are_on > 3
                    or number_of_neighbors_that_are_on < 2
                ):
                    grid_copy[y][x] = off_char
            else:
                if number_of_neighbors_that_are_on == 3:
                    grid_copy[y][x] = on_char
        grid = grid_copy


def number_of_lights_on():
    return sum(row.count(on_char) for row in grid)


with open(filename) as f:
    grid = [[c for c in line[:dimension]] for line in f]

animate(False)

print(f'Part 1: {number_of_lights_on()}')

with open(filename) as f:
    grid = [[c for c in line[:dimension]] for line in f]

for i, j in corner_coordinates:
    grid[j][i] = on_char

animate(True)

print(f'Part 2: {number_of_lights_on()}')
