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

import functools
import itertools
import operator
import sys

with open('input') as f:
    weights = [int(l.rstrip()) for l in f]


def solve(number_of_groups):
    group_weight = sum(weights) // number_of_groups
    least_quantum_entanglement = sys.maxsize
    for number_of_weights in range(1, len(weights)):
        for combo in itertools.combinations(weights, number_of_weights):
            if sum(combo) == group_weight:
                quantum_entanglement = functools.reduce(operator.mul, combo)
                if least_quantum_entanglement > quantum_entanglement:
                    least_quantum_entanglement = quantum_entanglement
        if least_quantum_entanglement != sys.maxsize:
            return least_quantum_entanglement


print(f'Part 1: {solve(3)}')
print(f'Part 2: {solve(4)}')
