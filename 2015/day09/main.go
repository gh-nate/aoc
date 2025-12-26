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
	"math"
	"os"
	"slices"
)

const format = "%s to %s = %d\n"

func main() {
	file, _ := os.Open(os.Args[len(os.Args)-1])

	var locations []string
	distances := make(map[[2]string]int)
	var location1, location2 string
	var distance int
	for {
		if _, err := fmt.Fscanf(file, format, &location1, &location2, &distance); err != nil {
			break
		}
		distances[[2]string{location1, location2}] = distance
		distances[[2]string{location2, location1}] = distance
		if !slices.Contains(locations, location1) {
			locations = append(locations, location1)
		}
		if !slices.Contains(locations, location2) {
			locations = append(locations, location2)
		}
	}

	shortestDistance := math.MaxInt
	longestDistance := 0
	for _, path := range permutations(locations) {
		distance = 0
		for i := range len(path) - 1 {
			distance += distances[[2]string{path[i], path[i+1]}]
		}
		shortestDistance = min(shortestDistance, distance)
		longestDistance = max(longestDistance, distance)
	}

	fmt.Println("Part 1:", shortestDistance)
	fmt.Println("Part 2:", longestDistance)
}

func permutations(locations []string) (paths [][]string) {
	// https://en.wikipedia.org/wiki/Heap%27s_algorithm
	var heaps func(int, []string)
	heaps = func(k int, a []string) {
		if k == 1 {
			paths = append(paths, slices.Clone(a))
		} else {
			j := k - 1
			heaps(j, a)
			for i := range j {
				if k%2 != 0 {
					i = 0
				}
				a[i], a[j] = a[j], a[i]
				heaps(j, a)
			}
		}
	}
	heaps(len(locations), locations)
	return
}
