package main

import (
	"fmt"
	"unicode/utf8"
)

func examineRune(r rune, arr *[]int, D *int, I *int) {

	if r == 'I' {
		*arr = append(*arr, *I)
		*I++
	} else if r == 'D' {
		*arr = append(*arr, *D)
		*D--
	}
}
func diStringMatch(s string) []int {

	var arr = []int{}
	D := len(s)
	I := 0

	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		examineRune(runeValue, &arr, &D, &I)
		w = width
	}
	arr = append(arr, D)
	return arr
}

func main() {
	var s = "IDID"
	fmt.Println(s)
	fmt.Println(diStringMatch(s))
}
