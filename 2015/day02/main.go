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
	"fmt"
	"os"
)

const format = "%dx%dx%d\n"

func main() {
	file, _ := os.Open(os.Args[len(os.Args)-1])

	var w, h, l, totalWrappingPaper, totalRibbon int
	for {
		if _, err := fmt.Fscanf(file, format, &l, &w, &h); err != nil {
			break
		}

		areaLw := l * w
		areaWh := w * h
		areaHl := h * l
		totalWrappingPaper += 2*areaLw + 2*areaWh + 2*areaHl + min(areaLw, areaWh, areaHl)

		perimeterLw := 2*l + 2*w
		perimeterWh := 2*w + 2*h
		perimeterHl := 2*h + 2*l
		totalRibbon += min(perimeterLw, perimeterWh, perimeterHl) + l*w*h
	}

	fmt.Println("Part 1:", totalWrappingPaper)
	fmt.Println("Part 2:", totalRibbon)
}
