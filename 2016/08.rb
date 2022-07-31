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
class Solution
  def initialize
    @screen = Array.new(6) { Array.new(50, false) }
    rect_regexp = /rect (\d+)x(\d+)/
    rotate_row_regexp = /rotate row y=(\d+) by (\d+)/
    rotate_column_regexp = /rotate column x=(\d+) by (\d+)/
    File.readlines('input').each do |instruction|
      m = rect_regexp.match(instruction)
      rect(m[1].to_i, m[2].to_i) unless m.nil?
      m = rotate_row_regexp.match(instruction)
      rotate_row(m[1].to_i, m[2].to_i) unless m.nil?
      m = rotate_column_regexp.match(instruction)
      rotate_column(m[1].to_i, m[2].to_i) unless m.nil?
    end
  end

  def number_of_pixels_lit = @screen.sum { |row| row.count(true) }

  def show
    @screen.each do |row|
      row.each { |column| print column ? '█' : ' ' }
      puts
    end
  end

  def rect(width, height)
    (0...height).each { |j| (0...width).each { |i| @screen[j][i] = true } }
  end

  def rotate_column(column_index, iterations)
    iterations.times do
      temporary = @screen.last[column_index]
      (1...@screen.count).reverse_each { |j| @screen[j][column_index] = @screen[j - 1][column_index] }
      @screen[0][column_index] = temporary
    end
  end

  def rotate_row(row_index, iterations)
    iterations.times do
      temporary = @screen[row_index].last
      (1...@screen[row_index].count).reverse_each { |i| @screen[row_index][i] = @screen[row_index][i - 1] }
      @screen[row_index][0] = temporary
    end
  end

  private :rect, :rotate_column, :rotate_row
end

solution = Solution.new
puts "Part 1: #{solution.number_of_pixels_lit}"
puts 'Part 2:'
solution.show
