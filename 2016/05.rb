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

require 'digest'

# :nodoc:
class Prompt
  attr_reader :input

  def initialize
    print 'Enter puzzle input: '
    @input = gets.chomp
  end
end

# :nodoc:
class SolutionPart1
  def initialize
    @password_length = 8
    @zeroes = '0' * 5
  end

  def password(door_id)
    previous_index = 0
    @password_length.times.reduce('') do |pw, _|
      (previous_index..).each do |index|
        digest = Digest::MD5.hexdigest("#{door_id}#{index}")
        next unless digest.start_with?(@zeroes)
        previous_index = index + 1
        break pw + digest[5]
      end
    end
  end
end

# :nodoc:
class SolutionPart2 < SolutionPart1
  def password(door_id)
    space = ' '
    pw = space * @password_length
    (0..).each do |index|
      digest = Digest::MD5.hexdigest("#{door_id}#{index}")
      next unless digest.start_with?(@zeroes)
      case digest[5]
      when '0', '1', '2', '3', '4', '5', '6', '7' then position = digest[5].to_i
      else next
      end
      pw[position] = digest[6] if pw[position] == space
      break pw if pw.delete(space).length == @password_length
    end
  end
end

door_id = Prompt.new.input
puts "Part 1: #{SolutionPart1.new.password(door_id)}"
puts "Part 2: #{SolutionPart2.new.password(door_id)}"
