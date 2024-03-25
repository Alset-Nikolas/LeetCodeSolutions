package main

import (
	"fmt"
	"math"
	"math/bits"
	"strconv"
	"unicode/utf8"
)

func replaceRuneInIndex(word *string, r rune, i int) {
	out := []rune(*word)
	out[i] = r
	*word = string(out)

}

func bitwiseComplement(n int) int {
	nBit := strconv.FormatInt(int64(n), 2)
	for i := 0; i < utf8.RuneCountInString(nBit); i++ {
		if nBit[i] == '1' {
			replaceRuneInIndex(&nBit, '0', i)
		} else {
			replaceRuneInIndex(&nBit, '1', i)
		}
	}
	fmt.Println(nBit)
	res, _ := strconv.ParseInt(nBit, 2, 64)
	return int(res)
}

func bitwiseComplementVAa2(n int) int {
	l := bits.Len(uint(n))
	tmp := math.Pow(2, float64(l)) - 1
	return n ^ int(tmp)
}

func main() {
	bitwiseComplementVAa2(10)

}
