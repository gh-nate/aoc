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
class IPAddr
  def initialize(ip)
    @hypernets = []
    @supernets = []
    substring = String.new
    ip.each_char do |c|
      case c
      when '['
        unless substring.empty?
          @supernets.append(-substring)
          substring.clear
        end
      when ']'
        unless substring.empty?
          @hypernets.append(-substring)
          substring.clear
        end
      else substring << c
      end
    end
    @supernets.append(-substring)
  end

  def support?(protocol)
    case protocol
    when :TLS then support_tls?
    when :SSL then support_ssl?
    end
  end

  def support_tls?
    @supernets.any? { |net| self.class.contains_abba?(net) } &&
      @hypernets.none? { |net| self.class.contains_abba?(net) }
  end

  def support_ssl?
    aba = Set.new
    @supernets.each do |supernet|
      supernet.each_char.each_cons(3) { |three| aba.add(three) if self.class.aba?(three) }
    end
    return false if aba.empty?
    bab = aba.map { |e| self.class.aba_to_bab(e) }
    @hypernets.any? { |hypernet| hypernet.each_char.each_cons(3).any? { |three| bab.include?(three) } }
  end

  private :support_ssl?, :support_tls?

  def self.contains_abba?(s) = s.each_char.each_cons(4).any? { |substring| abba?(substring) }

  def self.aba?(s) = s.count == 3 && s[0] != s[1] && s[0] == s[2]

  def self.abba?(s) = s.count == 4 && s[...2] == s[2..].reverse && s[0] != s[1]

  def self.aba_to_bab(s)
    raise "bad aba: #{s}" if s.count != 3
    [s[1], s[0], s[1]]
  end
end

# :nodoc:
class Solution
  def initialize
    @addresses = File.readlines('input').map { |ip| IPAddr.new(ip) }
  end

  def support_count(protocol) = @addresses.filter { |ip| ip.support?(protocol) }.count
end

solution = Solution.new
puts "Part 1: #{solution.support_count(:TLS)}"
puts "Part 2: #{solution.support_count(:SSL)}"
