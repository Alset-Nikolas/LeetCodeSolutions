package main

import (
	"fmt"
)

func sortArrayByParityII(nums []int) []int {
	j_start := 1
	for i := 0; i < len(nums); i += 2 {
		if nums[i]%2 != 0 {
			for j := j_start; j < len(nums); j += 2 {
				if nums[j]%2 == 0 {
					nums[i], nums[j] = nums[j], nums[i]
					j_start = j
					break
				}
			}
		}
	}
	return nums
}
func main() {
	var nums = []int{4, 2, 5, 7}
	res := sortArrayByParityII(
		nums,
	)

	fmt.Println(res)
}
