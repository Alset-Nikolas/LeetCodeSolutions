package main

import (
	"fmt"
)

func repeatedNTimes(nums []int) int {
	info := make(map[int]bool)
	for _, x := range nums {
		_, flag := info[x]
		if flag {
			return x
		}
		info[x] = true
	}
	return 0
}

func main() {
	var s = []int{1, 2, 3, 3}
	fmt.Println(s)
	fmt.Println(repeatedNTimes(s))
}
