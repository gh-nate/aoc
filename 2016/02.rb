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
class Keypad1CursorPosition
  def initialize
    @x = 0
    @y = 0
  end

  def move(direction)
    case direction
    when 'U' then @y += 1 if @y < 1
    when 'D' then @y -= 1 if @y > -1
    when 'L' then @x -= 1 if @x > -1
    when 'R' then @x += 1 if @x < 1
    end
  end

  def code
    case [@x, @y]
    when [-1, +1] then '1'
    when [+0, +1] then '2'
    when [+1, +1] then '3'
    when [-1, +0] then '4'
    when [+0, +0] then '5'
    when [+1, +0] then '6'
    when [-1, -1] then '7'
    when [+0, -1] then '8'
    when [+1, -1] then '9'
    end
  end
end

# :nodoc:
class Keypad2CursorPosition < Keypad1CursorPosition
  def initialize
    super
    @x = -2
  end

  def move(direction)
    case direction
    when 'U' then @y += 1 if @y < 2 - @x.abs
    when 'D' then @y -= 1 if @y > @x.abs - 2
    when 'L' then @x -= 1 if @x > @y.abs - 2
    when 'R' then @x += 1 if @x < 2 - @y.abs
    end
  end

  def code
    case [@x, @y]
    when [+0, +2] then '1'
    when [-1, +1] then '2'
    when [+0, +1] then '3'
    when [+1, +1] then '4'
    when [-2, +0] then '5'
    when [-1, +0] then '6'
    when [+0, +0] then '7'
    when [+1, +0] then '8'
    when [+2, +0] then '9'
    when [-1, -1] then 'A'
    when [+0, -1] then 'B'
    when [+1, -1] then 'C'
    when [+0, -2] then 'D'
    end
  end
end

# :nodoc:
class Solution
  def initialize(keypad)
    @instructions = open('input').readlines
    @position = keypad
  end

  def bathroom_code
    code = ''
    @instructions.each do |line|
      line.each_char { |char| @position.move(char) }
      code += @position.code
    end
    code
  end
end

puts "Part 1: #{Solution.new(Keypad1CursorPosition.new).bathroom_code}"
puts "Part 2: #{Solution.new(Keypad2CursorPosition.new).bathroom_code}"
