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
	"crypto/md5"
	"fmt"
	"io"
	"os"
	"strings"
)

func solve(input, prefix string, n int) int {
	for h := md5.New(); !strings.HasPrefix(fmt.Sprintf("%x", h.Sum(nil)), prefix); n++ {
		h.Reset()
		io.WriteString(h, fmt.Sprint(input, n))
	}
	return n - 1
}

func main() {
	input := os.Args[len(os.Args)-1]

	n := solve(input, "00000", 1)
	fmt.Println("Part 1:", n)
	fmt.Println("Part 2:", solve(input, "000000", n+1))
}
