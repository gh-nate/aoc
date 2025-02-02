/*
 * Copyright (c) 2025 gh-nate
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Action int

const (
	ActionUndefined Action = iota
	ActionTurnOff
	ActionTurnOn
	ActionToggle
)

var ActionPrefixes = map[string]Action{
	"turn off ": ActionTurnOff,
	"turn on ":  ActionTurnOn,
	"toggle ":   ActionToggle,
}

var re = regexp.MustCompile("([0-9]+)")

const SIZE int = 1000

func main() {
	f, err := os.Open(os.Args[len(os.Args)-1])
	if err != nil {
		os.Exit(1)
	}
	defer f.Close()

	var a Action
	var coordinates [4]int
	var brightness, lit uint
	var lights_part_1 [SIZE][SIZE]bool
	var lights_part_2 [SIZE][SIZE]int

	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		s := scanner.Text()
		a = ActionUndefined
		for prefix, action := range ActionPrefixes {
			if strings.HasPrefix(s, prefix) {
				a = action
				break
			}
		}
		if a == ActionUndefined {
			continue
		}
		for index, coordinate := range re.FindAllString(s, 4) {
			i, err := strconv.Atoi(coordinate)
			if err != nil {
				os.Exit(1)
			}
			coordinates[index] = i
		}
		switch a {
		case ActionTurnOff:
			for k := coordinates[0]; k <= coordinates[2]; k++ {
				for j := coordinates[1]; j <= coordinates[3]; j++ {
					if lights_part_1[j][k] {
						lights_part_1[j][k] = false
						lit--
					}
					if lights_part_2[j][k] > 0 {
						lights_part_2[j][k]--
						brightness--
					}
				}
			}
		case ActionTurnOn:
			for k := coordinates[0]; k <= coordinates[2]; k++ {
				for j := coordinates[1]; j <= coordinates[3]; j++ {
					if !lights_part_1[j][k] {
						lights_part_1[j][k] = true
						lit++
					}
					lights_part_2[j][k]++
					brightness++
				}
			}
		case ActionToggle:
			for k := coordinates[0]; k <= coordinates[2]; k++ {
				for j := coordinates[1]; j <= coordinates[3]; j++ {
					if lights_part_1[j][k] {
						lights_part_1[j][k] = false
						lit--
					} else {
						lights_part_1[j][k] = true
						lit++
					}
					lights_part_2[j][k] += 2
					brightness += 2
				}
			}
		}
	}

	if err := scanner.Err(); err != nil {
		os.Exit(1)
	}

	fmt.Println("Part 1:", lit)
	fmt.Println("Part 2:", brightness)
}
