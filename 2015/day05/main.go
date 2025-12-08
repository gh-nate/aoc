// Copyright (c) 2025 gh-nate
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func isNicePart1(s string) bool {
	var (
		numVowels            int
		p                    rune
		hasLetterAppearTwice bool
	)
	for _, c := range s {
		switch c {
		case 'a', 'e', 'i', 'o', 'u':
			numVowels += 1
		}
		if p == c {
			hasLetterAppearTwice = true
		}
		p = c
	}
	for i := range len(s) - 1 {
		switch s[i : i+2] {
		case "ab", "cd", "pq", "xy":
			return false
		}
	}
	return numVowels >= 3 && hasLetterAppearTwice
}

func isNicePart2(s string) bool {
	var hasNonOverlappingPairs bool
	pairs := make(map[string]int)
	for i := range len(s) - 1 {
		ss := s[i : i+2]
		j, ok := pairs[ss]
		if ok && i != j {
			hasNonOverlappingPairs = true
			break
		} else {
			pairs[ss] = i + 1
		}
	}
	var hasSandwich bool
	for i := range len(s) - 2 {
		if s[i] == s[i+2] {
			hasSandwich = true
			break
		}
	}
	return hasNonOverlappingPairs && hasSandwich
}

func main() {
	file, _ := os.Open(os.Args[len(os.Args)-1])
	var totalPart1, totalPart2 int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		if isNicePart1(s) {
			totalPart1 += 1
		}
		if isNicePart2(s) {
			totalPart2 += 1
		}
	}
	fmt.Println("Part 1:", totalPart1)
	fmt.Println("Part 2:", totalPart2)
}
