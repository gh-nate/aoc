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
	"strconv"
)

const (
	opLshift = iota
	opRshift
	opAnd
	opOr
	opNot
	opAssign
	base    = 10
	bitSize = 16
)

type gate struct {
	lhs, rhs any
	op       int
	id       string
}

func main() {
	formats := [6]string{
		"%s LSHIFT %s -> %s",
		"%s RSHIFT %s -> %s",
		"%s AND %s -> %s",
		"%s OR %s -> %s",
		"NOT %s -> %s",
		"%s -> %s",
	}
	var gates []gate
	wires := make(map[string]uint16)

	var lhs, rhs, id, format string
	var op int

	file, _ := os.Open(os.Args[len(os.Args)-1])
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
	FormatsLoop:
		for op, format = range formats {
			switch op {
			case opLshift, opRshift, opAnd, opOr:
				n, err := fmt.Sscanf(s, format, &lhs, &rhs, &id)
				if n == 3 && err == nil {
					gates = append(gates, gate{lhs, rhs, op, id})
					break FormatsLoop
				}
			case opNot, opAssign:
				n, err := fmt.Sscanf(s, format, &rhs, &id)
				if n == 2 && err == nil {
					if op == opAssign {
						if signal, err := strconv.ParseUint(rhs, base, bitSize); err == nil {
							wires[id] = uint16(signal)
							break FormatsLoop
						}
					}
					gates = append(gates, gate{err, rhs, op, id})
					break FormatsLoop
				}
			}
		}
	}

	var aSignal uint16
AssembleLoop:
	for {
		if signal, ok := wires["a"]; ok {
			aSignal = signal
			break AssembleLoop
		}
	}

	fmt.Println("Part 1:", aSignal)
	// fmt.Println("Part 2:", 0)
}
