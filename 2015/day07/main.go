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
	"strconv"
	"strings"
)

type Wire struct {
	id     string
	signal any
}

type NotGate Wire

type BitwiseOp int

const (
	BitwiseAND BitwiseOp = iota
	BitwiseOR
	BitwiseLSHIFT
	BitwiseRSHIFT
)

var BitwiseOpRep = map[string]BitwiseOp{
	"AND":    BitwiseAND,
	"OR":     BitwiseOR,
	"LSHIFT": BitwiseLSHIFT,
	"RSHIFT": BitwiseRSHIFT,
}

type BinGate struct {
	lhs any
	op  BitwiseOp
	rhs any
	dst string
}

func assemble(binGates []BinGate, notGates []NotGate, wires []Wire) uint16 {
	for {
		for i := 0; i < len(wires); i++ {
			wire1 := wires[i]
			if v, ok := wire1.signal.(uint16); ok {
				if wire1.id == "a" {
					return v
				}
				for j, binGate := range binGates {
					if s, ok := binGate.lhs.(string); ok && s == wire1.id {
						binGates[j].lhs = v
					}
					if s, ok := binGate.rhs.(string); ok && s == wire1.id {
						binGates[j].rhs = v
					}
				}
				for j, notGate := range notGates {
					if s, ok := notGate.signal.(string); ok && s == wire1.id {
						notGates[j].signal = v
					}
				}
				for j, wire2 := range wires[:i] {
					if s, ok := wire2.signal.(string); ok && s == wire1.id {
						wires[j].signal = v
					}
				}
				for j, wire2 := range wires[i+1:] {
					if s, ok := wire2.signal.(string); ok && s == wire1.id {
						wires[j].signal = v
					}
				}
				wires = append(wires[:i], wires[i+1:]...)
				i--
			}
		}
		for i := 0; i < len(binGates); i++ {
			binGate := binGates[i]
			lhs, ok1 := binGate.lhs.(uint16)
			rhs, ok2 := binGate.rhs.(uint16)
			if ok1 && ok2 {
				switch binGate.op {
				case BitwiseAND:
					lhs &= rhs
				case BitwiseOR:
					lhs |= rhs
				case BitwiseLSHIFT:
					lhs <<= rhs
				case BitwiseRSHIFT:
					lhs >>= rhs
				}
				wires = append(wires, Wire{binGate.dst, lhs})
				binGates = append(binGates[:i], binGates[i+1:]...)
				i--
			}
		}
		for i := 0; i < len(notGates); i++ {
			notGate := notGates[i]
			if v, ok := notGate.signal.(uint16); ok {
				wires = append(wires, Wire{notGate.id, ^v})
				notGates = append(notGates[:i], notGates[i+1:]...)
				i--
			}
		}
	}
}

const (
	BASE      int    = 10
	BITSIZE   int    = 16
	DELIMITER string = " "
)

func convert(scanner *bufio.Scanner) (binGates []BinGate, notGates []NotGate, wires []Wire) {
	for scanner.Scan() {
		s := scanner.Text()
		if strings.Contains(s, "AND") || strings.Contains(s, "OR") || strings.Contains(s, "SHIFT") {
			gate := BinGate{}
			items := strings.Split(s, DELIMITER)
			gate.lhs = items[0]
			i, err := strconv.ParseUint(items[0], BASE, BITSIZE)
			if err == nil {
				gate.lhs = uint16(i)
			}
			gate.op = BitwiseOpRep[items[1]]
			gate.rhs = items[2]
			i, err = strconv.ParseUint(items[2], BASE, BITSIZE)
			if err == nil {
				gate.rhs = uint16(i)
			}
			gate.dst = items[4]
			binGates = append(binGates, gate)
		} else if strings.HasPrefix(s, "NOT") {
			gate := NotGate{}
			items := strings.Split(s, DELIMITER)
			gate.signal = items[1]
			i, err := strconv.ParseUint(items[1], BASE, BITSIZE)
			if err == nil {
				gate.signal = uint16(i)
			}
			gate.id = items[3]
			notGates = append(notGates, gate)
		} else if strings.Contains(s, "->") {
			wire := Wire{}
			items := strings.Split(s, DELIMITER)
			wire.signal = items[0]
			i, err := strconv.ParseUint(items[0], BASE, BITSIZE)
			if err == nil {
				wire.signal = uint16(i)
			}
			wire.id = items[2]
			wires = append(wires, wire)
		}
	}

	if err := scanner.Err(); err != nil {
		os.Exit(1)
	}

	return
}

func main() {
	f, err := os.Open(os.Args[len(os.Args)-1])
	if err != nil {
		os.Exit(1)
	}
	defer f.Close()

	binGatesP1, notGatesP1, wiresP1 := convert(bufio.NewScanner(f))

	binGatesP2 := make([]BinGate, len(binGatesP1))
	copy(binGatesP2, binGatesP1)
	notGatesP2 := make([]NotGate, len(notGatesP1))
	copy(notGatesP2, notGatesP1)
	wiresP2 := make([]Wire, len(wiresP1))
	copy(wiresP2, wiresP1)

	a := assemble(binGatesP1, notGatesP1, wiresP1)

	fmt.Println("Part 1:", a)

	for i, wire := range wiresP2 {
		if wire.id == "b" {
			wiresP2[i].signal = a
			break
		}
	}
	a = assemble(binGatesP2, notGatesP2, wiresP2)
	fmt.Println("Part 2:", a)
}
