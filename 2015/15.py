# Copyright (c) 2022 gh-nate
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without max_sumation the rights
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

from dataclasses import dataclass

import functools
import operator
import re

with open('input') as f:
    descriptions = f.readlines()

pattern = '(\w+): '
for property in ['capacity', 'durability', 'flavor', 'texture', 'calories']:
    pattern += f'{property} (-*\d+), '

o = re.compile(pattern[:-2])


@dataclass(frozen=True)
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


ingredients = []
for description in descriptions:
    if m := o.match(description):
        n, c_1, d, f, t, c_2 = m.groups()
        ingredients.append(Ingredient(n, int(c_1), int(d), int(f), int(t), int(c_2)))


max_depth = len(ingredients)
max_score = 0
max_score_with_calories_considered = 0
max_sum = 100


def evaluate_combination(l):
    global max_score, max_score_with_calories_considered
    properties = [0 for _ in range(5)]
    for index, amount in enumerate(l):
        properties[0] += amount * ingredients[index].capacity
        properties[1] += amount * ingredients[index].durability
        properties[2] += amount * ingredients[index].flavor
        properties[3] += amount * ingredients[index].texture
        properties[4] += amount * ingredients[index].calories
    for index, property in enumerate(properties):
        if property < 0:
            properties[index] = 0
    score = functools.reduce(operator.mul, properties[:-1])
    if score > max_score:
        max_score = score
    if properties[4] == 500 and score > max_score_with_calories_considered:
        max_score_with_calories_considered = score


def find_combinations(values, branch):
    if len(branch) == max_depth:
        if sum(branch) == max_sum:
            evaluate_combination(branch)
    else:
        for i, v in enumerate(values):
            find_combinations(values[:i] + values[i + 1 :], branch + [v])


find_combinations([n for n in range(max_sum + 1)], [])

print(f'Part 1: {max_score}')
print(f'Part 2: {max_score_with_calories_considered}')
