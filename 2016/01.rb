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

require 'set'

# :nodoc:
class Position
  attr_accessor :x, :y

  def initialize
    @x = 0
    @y = 0
  end

  def distance_from_origin = @x.abs + @y.abs

  def to_a = [@x, @y]
end

# :nodoc:
class SolutionPart1
  def initialize
    @instructions = File.read('input').rstrip.split(', ')
    @position = Position.new
    @direction = :NORTH
  end

  def move(left_or_right, number_of_blocks)
    case [@direction, left_or_right]
    when %i[NORTH LEFT], %i[SOUTH RIGHT]
      @position.x -= number_of_blocks
      @direction = :WEST
    when %i[NORTH RIGHT], %i[SOUTH LEFT]
      @position.x += number_of_blocks
      @direction = :EAST
    when %i[EAST LEFT], %i[WEST RIGHT]
      @position.y += number_of_blocks
      @direction = :NORTH
    when %i[EAST RIGHT], %i[WEST LEFT]
      @position.y -= number_of_blocks
      @direction = :SOUTH
    end
  end

  def shortest_distance_to_easter_bunny_hq
    regexp = /(L|R)(\d+)/
    @instructions.map { |i| regexp.match(i) }.each do |m|
      case m[1]
      when 'L' then move(:LEFT, m[2].to_i)
      when 'R' then move(:RIGHT, m[2].to_i)
      end
    end
    @position.distance_from_origin
  end
end

# :nodoc:
class SolutionPart2 < SolutionPart1
  def initialize
    super
    @visited = Set[@position.to_a]
    @found_hq = false
  end

  def move(left_or_right, number_of_blocks)
    return if @found_hq
    case [@direction, left_or_right]
    when %i[NORTH LEFT], %i[SOUTH RIGHT]
      number_of_blocks.times do
        @position.x -= 1
        break @found_hq = true unless @visited.add?(@position.to_a)
      end
      @direction = :WEST
    when %i[NORTH RIGHT], %i[SOUTH LEFT]
      number_of_blocks.times do
        @position.x += 1
        break @found_hq = true unless @visited.add?(@position.to_a)
      end
      @direction = :EAST
    when %i[EAST LEFT], %i[WEST RIGHT]
      number_of_blocks.times do
        @position.y += 1
        break @found_hq = true unless @visited.add?(@position.to_a)
      end
      @direction = :NORTH
    when %i[EAST RIGHT], %i[WEST LEFT]
      number_of_blocks.times do
        @position.y -= 1
        break @found_hq = true unless @visited.add?(@position.to_a)
      end
      @direction = :SOUTH
    end
  end
end

puts "Part 1: #{SolutionPart1.new.shortest_distance_to_easter_bunny_hq}"
puts "Part 2: #{SolutionPart2.new.shortest_distance_to_easter_bunny_hq}"
