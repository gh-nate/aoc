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

with open('input') as f:
    guest_list = f.readlines()

o = re.compile('(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).')

guests = set()
happiness = {}

for description in guest_list:
    if m := o.match(description):
        guest_1, reaction, units, guest_2 = m.groups()
        guests.add(guest_1)
        happiness[(guest_1, guest_2)] = (
            int(units) if reaction == 'gain' else -int(units)
        )


def optimal_change_in_happiness(guests, happiness):
    deltas = []
    for p in itertools.permutations(guests):
        units = 0
        for i in range(-1, len(p) - 1):
            guest_1, guest_2 = p[i], p[i + 1]
            units += happiness[(guest_1, guest_2)]
            units += happiness[(guest_2, guest_1)]
        deltas.append(units)
    return max(deltas)


change_1 = optimal_change_in_happiness(guests, happiness)

me = 'I/me'
for guest in guests:
    happiness[(guest, me)] = happiness[(me, guest)] = 0
guests.add(me)

change_2 = optimal_change_in_happiness(guests, happiness)

print(f'Part 1: {change_1}')
print(f'Part 2: {change_2}')
