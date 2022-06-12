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
    descriptions = f.readlines()


class Reindeer:
    def __init__(self, name, speed, fly_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration
        self.points = 0
        self._travelled = self._travel()

    def travel(self):
        return next(self._travelled)

    def _travel(self):
        travelled = 0
        while True:
            fly_duration = self.fly_duration
            while fly_duration > 0:
                travelled += self.speed
                fly_duration -= 1
                yield travelled
            rest_duration = self.rest_duration
            while rest_duration > 0:
                rest_duration -= 1
                yield travelled


o = re.compile(
    '(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
)

reindeers = []
for description in descriptions:
    if m := o.match(description):
        name, speed, fly_duration, rest_duration = m.groups()
        reindeers.append(
            Reindeer(name, int(speed), int(fly_duration), int(rest_duration))
        )

for _ in range(2503):  # duration
    distances = [r.travel() for r in reindeers]
    furthest = max(distances)
    for i, r in enumerate(reindeers):
        if distances[i] == furthest:
            r.points += 1

print(f'Part 1: {furthest}')
print(f'Part 2: {max(r.points for r in reindeers)}')
