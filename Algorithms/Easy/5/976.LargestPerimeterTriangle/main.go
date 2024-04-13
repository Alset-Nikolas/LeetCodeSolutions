package main

import (
	"fmt"
	"sort"
)

func largestPerimeter(nums []int) int {
	res := 0
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	for i := 1; i < len(nums)-1; i++ {
		if nums[i-1] < nums[i]+nums[i+1] {
			if res < nums[i-1]+nums[i]+nums[i+1] {
				res = nums[i] + nums[i+1] + nums[i-1]
			}
		}
	}
	return res
}

func main() {
	var mass = []int{1, 2, 3}
	fmt.Println(largestPerimeter(mass))

}
