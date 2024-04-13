package main

import (
	"fmt"
	"strings"
)

func reverseOnlyLetters(s string) string {
	mass := strings.Split(s, "")
	j := len(mass) - 1

	for i := 0; i < j; i++ {
		var lower_litter_i, lower_litter_j string = strings.ToLower(mass[i]), strings.ToLower(mass[j])
		for i < j && (lower_litter_i < "a" || lower_litter_i > "z") {
			i++
			lower_litter_i = strings.ToLower(mass[i])
		}
		for i < j && (lower_litter_j < "a" || lower_litter_j > "z") {
			j--
			lower_litter_j = strings.ToLower(mass[j])
		}
		if i >= j {
			break
		}
		mass[i], mass[j] = mass[j], mass[i]
		j--
	}

	return strings.Join(mass, "")
}
func main() {
	var text string = "ab-cd"
	res := reverseOnlyLetters(
		text,
	)

	fmt.Println(res)
}
