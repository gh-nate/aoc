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
    @list = File.readlines('input')
  end

  def self.checksum(s)
    h = Hash.new('')
    s.delete('-').each_char do |c|
      count = s.count(c)
      h[count] += c unless h[count].include?(c)
    end
    h.sort.reverse.reduce('') { |r, a| r + a.last.each_char.sort.join }[..4]
  end

  def real_rooms
    regexp = /(.*)(\d{3})\[([a-z]{5})\]/
    @list.map { |i| regexp.match(i) }.filter { |m| self.class.checksum(m[1]) == m[3] }
  end

  protected :real_rooms

  def sum = real_rooms.sum { |m| m[2].to_i }
end

# :nodoc:
class SolutionPart2 < SolutionPart1
  def sector_id(real_name)
    real_rooms.each do |m|
      sector_id = m[2].to_i
      rotations = sector_id % 26
      name = m[1].each_char.reduce('') do |r, c|
        if c == '-'
          "#{r} "
        else
          rotations.times { c.succ! }
          r + c[-1]
        end
      end
      return sector_id if name == real_name
    end
  end
end

puts "Part 1: #{SolutionPart1.new.sum}"
puts "Part 2: #{SolutionPart2.new.sector_id('northpole object storage ')}"
