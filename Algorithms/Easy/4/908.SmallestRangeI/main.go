package main

import (
	"fmt"
	"sort"
)

func smallestRangeI(nums []int, k int) int {
	sort.Ints(nums)
	l, h := nums[0], nums[len(nums)-1]
	if h-l <= 2*k {
		return 0
	}

	return h - l - 2*k
}

func main() {
	var nums = []int{3, 1, 10}
	var k int = 4

	res := smallestRangeI(
		nums, k,
	)
	fmt.Println(res)
}
