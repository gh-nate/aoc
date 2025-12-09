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

type point struct {
	x int
	y int
}

func main() {
	data, _ := os.ReadFile(os.Args[len(os.Args)-1])

	var santa point
	visited := map[point]bool{santa: true}
	for _, b := range data {
		switch b {
		case '^':
			santa.y++
		case 'v':
			santa.y--
		case '>':
			santa.x++
		case '<':
			santa.x--
		}
		visited[santa] = true
	}

	fmt.Println("Part 1:", len(visited))

	clear(visited)
	santa.x = 0
	santa.y = 0
	visited[santa] = true
	var (
		robot point
		who   *point
	)

	for i, b := range data {
		if i%2 == 0 {
			who = &santa
		} else {
			who = &robot
		}
		switch b {
		case '^':
			who.y++
		case 'v':
			who.y--
		case '>':
			who.x++
		case '<':
			who.x--
		}
		visited[*who] = true
	}

	fmt.Println("Part 2:", len(visited))
}
