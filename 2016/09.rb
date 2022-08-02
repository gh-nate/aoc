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
    @data = File.read('input').each_char.to_a
  end

  def decompressed_size
    size = 0
    index = 0
    while index < @data.size
      case @data[index]
      when "\n" then index += 1
      when '('
        length = String.new
        until @data[index] == 'x'
          index += 1
          length << @data[index]
        end
        repeat = String.new
        until @data[index] == ')'
          index += 1
          repeat << @data[index]
        end
        size += repeat.to_i * length.to_i
        index += length.to_i + 1
      else
        size += 1
        index += 1
      end
    end
    size
  end
end

# :nodoc:
class SolutionPart2 < SolutionPart1
  def decompressed_size
    count = 0
    until @data.empty?
      index = 0
      case @data[index]
      when "\n" then index += 1
      when '('
        length = String.new
        until @data[index] == 'x'
          index += 1
          length << @data[index]
        end
        repeat = String.new
        until @data[index] == ')'
          index += 1
          repeat << @data[index]
        end
        index += 1
        length = length.to_i
        end_index = index + length
        ss = @data[index...end_index]
        repeat.to_i.times { @data.insert(end_index, *ss) }
        index += length
      else
        index += 1
        count += 1
      end
      @data.shift(index)
    end
    count
  end
end

puts "Part 1: #{SolutionPart1.new.decompressed_size}"
puts "Part 2: #{SolutionPart2.new.decompressed_size}"
