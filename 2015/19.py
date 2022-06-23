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

o = re.compile('(\w+) => (\w+)')
molecule_replacements = {}

with open('input') as f:
    for l in f:
        if m := o.match(l):
            molecule, replacement = m.groups()
            values = molecule_replacements.setdefault(molecule, [])
            values.append(replacement)
        else:
            medicine = l.rstrip()

molecules = set()
length_medicine = len(medicine)
for molecule, replacements in molecule_replacements.items():
    length_molecule = len(molecule)
    for i in range(length_medicine - length_molecule):
        if molecule == medicine[i : i + length_molecule]:
            for replacement in replacements:
                molecules.add(
                    medicine[:i] + replacement + medicine[i + length_molecule :]
                )

print(f'Part 1: {len(molecules)}')

molecules_lengths = {}
reversed_molecule_replacements = {}
for molecule, replacements in molecule_replacements.items():
    for replacement in replacements:
        reversed_molecule_replacements[replacement] = molecule
        molecules_lengths[replacement] = len(replacement)

molecules = []
for length_1 in sorted(set(molecules_lengths.values()), reverse=True):
    for molecule, length_2 in molecules_lengths.items():
        if length_1 == length_2:
            molecules.append(molecule)

steps = 0
while medicine != 'e':
    length_medicine = len(medicine)
    for molecule in molecules:
        length_molecule = molecules_lengths[molecule]
        for i in range(length_medicine - length_molecule):
            if molecule == medicine[i : i + length_molecule]:
                medicine = (
                    medicine[:i]
                    + reversed_molecule_replacements[molecule]
                    + medicine[i + length_molecule :]
                )
                steps += 1
                break

print(f'Part 2: {steps}')
