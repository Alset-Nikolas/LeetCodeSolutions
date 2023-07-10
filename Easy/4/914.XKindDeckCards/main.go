package main

import (
	"fmt"
)

func hasGroupsSizeX(deck []int) bool {
	info := make(map[int]int)
	for i := 0; i < len(deck); i++ {
		value, flag := info[deck[i]]
		if !flag {
			info[deck[i]] = 0
		}
		info[deck[i]] = value + 1

	}
	res := make(map[int]bool)
	for i := info[deck[0]]; i >= 2; i-- {
		if info[deck[0]]%i == 0 {
			res[i] = true
		}
	}

	for _, n := range info { // Порядок не определен
		for y, flag := range res {
			if flag && n%y != 0 {
				res[y] = false

			}

		}

	}
	for _, flag := range res {
		if flag {
			return true
		}
	}

	return false

}
func main() {
	var deck = []int{1, 2, 3, 4, 4, 3, 2, 1}
	res := hasGroupsSizeX(
		deck,
	)

	fmt.Println(res)
}
