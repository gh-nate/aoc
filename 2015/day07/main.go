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
	"slices"
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

var formats = [6]string{
	"%s LSHIFT %s -> %s",
	"%s RSHIFT %s -> %s",
	"%s AND %s -> %s",
	"%s OR %s -> %s",
	"NOT %s -> %s",
	"%s -> %s",
}

type gate struct {
	lhs, rhs any
	op       int
	id       string
}

func assemble(gates []gate, wires map[string]uint16) (aSignal uint16) {
	for {
		if signal, ok := wires["a"]; ok {
			aSignal = signal
			return
		}
		var assembledGateIndices []int
		for i, gate := range gates {
			var id string
			var isLhsId, isRhsId bool
			if id, isLhsId = gate.lhs.(string); isLhsId {
				if signal, ok := wires[id]; ok {
					gates[i].lhs = signal
					isLhsId = false
				}
			}
			if id, isRhsId = gate.rhs.(string); isRhsId {
				if signal, ok := wires[id]; ok {
					gates[i].rhs = signal
					isRhsId = false
				}
			}
			if !isLhsId && !isRhsId {
				gate = gates[i]
				switch gate.op {
				case opLshift:
					wires[gate.id] = gate.lhs.(uint16) << gate.rhs.(uint16)
				case opRshift:
					wires[gate.id] = gate.lhs.(uint16) >> gate.rhs.(uint16)
				case opAnd:
					wires[gate.id] = gate.lhs.(uint16) & gate.rhs.(uint16)
				case opOr:
					wires[gate.id] = gate.lhs.(uint16) | gate.rhs.(uint16)
				case opNot:
					wires[gate.id] = ^gate.rhs.(uint16)
				case opAssign:
					wires[gate.id] = gate.rhs.(uint16)
				}
				assembledGateIndices = append(assembledGateIndices, i)
			}
		}
		for _, i := range slices.Backward(assembledGateIndices) {
			gates = slices.Delete(gates, i, i+1)
		}
	}
}

func main() {
	input := os.Args[len(os.Args)-1]

	gates, wires := parse(input)
	aSignal := assemble(gates, wires)
	fmt.Println("Part 1:", aSignal)

	gates, wires = parse(input)
	wires["b"] = aSignal
	fmt.Println("Part 2:", assemble(gates, wires))
}

func parse(input string) (gates []gate, wires map[string]uint16) {
	wires = make(map[string]uint16)

	file, _ := os.Open(input)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
	FormatsLoop:
		for op, format := range formats {
			var lhs, rhs, id string
			switch op {
			case opLshift, opRshift, opAnd, opOr:
				n, err := fmt.Sscanf(s, format, &lhs, &rhs, &id)
				if n == 3 && err == nil {
					gate := gate{lhs, rhs, op, id}
					if signal, err := strconv.ParseUint(lhs, base, bitSize); err == nil {
						gate.lhs = uint16(signal)
					}
					if signal, err := strconv.ParseUint(rhs, base, bitSize); err == nil {
						gate.rhs = uint16(signal)
					}
					gates = append(gates, gate)
					break FormatsLoop
				}
			case opNot, opAssign:
				n, err := fmt.Sscanf(s, format, &rhs, &id)
				if n == 2 && err == nil {
					if signal, err := strconv.ParseUint(rhs, base, bitSize); err == nil {
						switch op {
						case opNot:
							wires[id] = ^uint16(signal)
						case opAssign:
							wires[id] = uint16(signal)
						}
					} else {
						gates = append(gates, gate{nil, rhs, op, id})
					}
					break FormatsLoop
				}
			}
		}
	}

	return
}
