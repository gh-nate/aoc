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

import operator
import re

filename = 'input'

with open(filename) as f:
    instructions = f.readlines()

and_ = re.compile('(-*\w+) AND (-*\w+) -> (\w+)')
or_ = re.compile('(-*\w+) OR (-*\w+) -> (\w+)')
lshift = re.compile('(-*\w+) LSHIFT (-*\w+) -> (\w+)')
rshift = re.compile('(-*\w+) RSHIFT (-*\w+) -> (\w+)')
not_ = re.compile('NOT (-*\w+) -> (\w+)')
assign = re.compile('(-*\w+) -> (\w+)')


def substitute(wire, signal):
    for i, instruction in enumerate(instructions):
        substituted = False
        components = instruction.split()
        for j, component in enumerate(components):
            if component == wire:
                substituted = True
                components[j] = str(signal)
        if substituted:
            instructions[i] = ' '.join(components)


def do_1(op, groups):
    signal, wire = groups
    try:
        signal = int(signal)
    except ValueError:
        return None
    if op == 'not':
        signal = ~signal
    substitute(wire, signal)
    return signal, wire


def do_2(op, groups):
    lhs, rhs, wire = groups
    try:
        lhs = int(lhs)
        rhs = int(rhs)
    except ValueError:
        return None
    signal = op(lhs, rhs)
    substitute(wire, signal)
    return signal, wire


def resolve():
    while instruction := instructions.pop():
        do = do_2
        if m := and_.match(instruction):
            op = operator.and_
        elif m := or_.match(instruction):
            op = operator.or_
        elif m := lshift.match(instruction):
            op = operator.lshift
        elif m := rshift.match(instruction):
            op = operator.rshift
        elif m := not_.match(instruction):
            do = do_1
            op = 'not'
        elif m := assign.match(instruction):
            do = do_1
            op = 'assign'
        if replaced := do(op, m.groups()):
            if replaced[1] == 'a':
                return replaced[0]
        else:
            instructions.insert(0, instruction)


a = resolve()

print(f'Part 1: {a}')

with open(filename) as f:
    instructions = f.readlines()

substitute('b', a)

print(f'Part 2: {resolve()}')
