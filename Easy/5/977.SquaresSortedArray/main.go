package main

import (
	"fmt"
)

func sortedSquares(nums []int) []int {
	i, j := 0, 0
	for i < len(nums) {
		if nums[i] >= 0 {
			break
		}
		i++

	}
	res := []int{}
	for i < len(nums) {
		if nums[i] == 0 {
			res = append(res, 0)
			i++
		} else {
			if j < 0 {
				res = append(res, nums[i]*nums[i])
				i++
			} else {
				if nums[i]^2 < nums[j]^2 {
					res = append(res, nums[i]*nums[i])
					i++
				} else {
					res = append(res, nums[j]*nums[j])
					j--
				}
			}
		}
	}
	for j > 0 {
		res = append(res, nums[j]*nums[j])
		j--
	}
	return res

}
func main() {
	var mass = []int{-3, -2, -1, 0, 0, 0, 1, 2, 3}
	fmt.Println(sortedSquares(mass))

}
