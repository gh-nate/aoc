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
    dimensions = f.readlines()

wrapping_paper = 0
ribbon = 0
for dimension in dimensions:
    l = [int(d) for d in dimension.rstrip().split('x')]
    area_lw = l[0] * l[1]
    area_wh = l[1] * l[2]
    area_hl = l[2] * l[0]
    wrapping_paper += 2 * area_lw + 2 * area_wh + 2 * area_hl  # surface area
    wrapping_paper += min(area_lw, area_wh, area_hl)  # area of smallest side
    ribbon += area_lw * l[2]  # volume
    l.remove(max(l))
    ribbon += l[0] * 2 + l[1] * 2  # smallest perimeter

print(f'Part 1: {wrapping_paper}')
print(f'Part 2: {ribbon}')
