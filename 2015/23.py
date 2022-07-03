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

offset = '([-|+]\d+)'
register = '([ab])'

hlf = re.compile(f'hlf {register}')
tpl = re.compile(f'tpl {register}')
inc = re.compile(f'inc {register}')
jmp = re.compile(f'jmp {offset}')
jie = re.compile(f'jie {register}, {offset}')
jio = re.compile(f'jio {register}, {offset}')


def run_program(a):
    b = 0
    index = 0
    while index < len(instructions):
        instruction = instructions[index]
        step = 1
        if m := hlf.match(instruction):
            match m.groups():
                case ('a',):
                    a /= 2
                case ('b',):
                    b /= 2
        elif m := tpl.match(instruction):
            match m.groups():
                case ('a',):
                    a *= 3
                case ('b',):
                    b *= 3
        elif m := inc.match(instruction):
            match m.groups():
                case ('a',):
                    a += 1
                case ('b',):
                    b += 1
        elif m := jmp.match(instruction):
            step = int(m.groups()[0])
        elif m := jie.match(instruction):
            r, o = m.groups()
            if (r == 'a' and a % 2 == 0) or (r == 'b' and b % 2 == 0):
                step = int(o)
        elif m := jio.match(instruction):
            r, o = m.groups()
            if (r == 'a' and a == 1) or (r == 'b' and b == 1):
                step = int(o)
        index += step
    return b


print(f'Part 1: {run_program(0)}')
print(f'Part 2: {run_program(1)}')
