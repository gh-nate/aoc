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
	"strings"
)

const (
	toggle = iota
	turnOff
	turnOn
	format    = "%d,%d through %d,%d"
	dimension = 1000
)

var prefixes = [3]string{"toggle", "turn off", "turn on"}

func main() {
	var (
		lightsPart1     [dimension][dimension]bool
		lightsPart2     [dimension][dimension]int
		rowPart1        *[dimension]bool
		rowPart2        *[dimension]int
		x1, y1, x2, y2  int
		action          int
		lit, brightness int
	)
	file, _ := os.Open(os.Args[len(os.Args)-1])
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		for i, prefix := range prefixes {
			s, found := strings.CutPrefix(s, prefix)
			if found {
				action = i
				fmt.Sscanf(s, format, &x1, &y1, &x2, &y2)
				break
			}
		}
		for ; y1 <= y2; y1++ {
			rowPart1 = &lightsPart1[y1]
			rowPart2 = &lightsPart2[y1]
			for i := x1; i <= x2; i++ {
				switch action {
				case toggle:
					if rowPart1[i] {
						rowPart1[i] = false
						lit--
					} else {
						rowPart1[i] = true
						lit++
					}
					rowPart2[i] += 2
					brightness += 2
				case turnOff:
					if rowPart1[i] {
						rowPart1[i] = false
						lit--
					}
					if rowPart2[i] > 0 {
						rowPart2[i]--
						brightness--
					}
				case turnOn:
					if !rowPart1[i] {
						rowPart1[i] = true
						lit++
					}
					rowPart2[i]++
					brightness++
				}
			}
		}
	}

	fmt.Println("Part 1:", lit)
	fmt.Println("Part 2:", brightness)
}
