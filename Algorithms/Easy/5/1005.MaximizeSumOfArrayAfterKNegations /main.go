package main

import "sort"

func minInt(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func sumSlice(nums []int) int {
	res := 0
	for i := 0; i < len(nums); i++ {
		res += nums[i]
	}
	return res
}
func getMinSlice(nums []int) int {
	x := nums[0]
	for i := 1; i < len(nums); i++ {
		x = minInt(x, nums[i])
	}
	return x
}
func largestSumAfterKNegations(nums []int, k int) int {
	sort.Ints(nums)
	negative := 0
	zeros := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] < 0 {
			negative++
		} else if nums[i] == 0 {
			zeros++
		}
	}

	if negative > 0 {
		for i := 0; i < minInt(negative, k); i++ {
			nums[i] *= -1
		}
		if negative > k {
			return sumSlice(nums)
		}
		k -= negative
	}
	if zeros > 0 || k%2 == 0 {
		return sumSlice(nums)
	}
	return sumSlice(nums) - getMinSlice(nums)*2
}

func main() {

}
