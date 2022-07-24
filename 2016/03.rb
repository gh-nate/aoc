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

# frozen_string_literal: true

# :nodoc:
class SolutionPart1
  def initialize
    @instructions = open('input').readlines
    @regexp = /(\d+)\s+(\d+)\s+(\d+)/
  end

  def triangle?(side1, side2, side3)
    side1 + side2 > side3 &&
      side2 + side3 > side1 &&
      side3 + side1 > side2
  end

  def number_of_possible_triangles
    @instructions.map { |i| @regexp.match(i) }.count do |m|
      triangle?(m[1].to_i, m[2].to_i, m[3].to_i)
    end
  end
end

# :nodoc:
class SolutionPart2 < SolutionPart1
  def number_of_possible_triangles
    count = 0
    @instructions.map { |i| @regexp.match(i) }.each_slice(3) do |tm|
      count += 1 if triangle?(tm[0][1].to_i, tm[1][1].to_i, tm[2][1].to_i)
      count += 1 if triangle?(tm[0][2].to_i, tm[1][2].to_i, tm[2][2].to_i)
      count += 1 if triangle?(tm[0][3].to_i, tm[1][3].to_i, tm[2][3].to_i)
    end
    count
  end
end

puts "Part 1: #{SolutionPart1.new.number_of_possible_triangles}"
puts "Part 2: #{SolutionPart2.new.number_of_possible_triangles}"
