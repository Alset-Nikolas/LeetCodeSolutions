package main

import (
	"fmt"
)

func validMountainArray(arr []int) bool {
	if len(arr) < 3 {
		return false
	}
	i, j := 1, len(arr)-1
	for i < len(arr) {
		if arr[i] < arr[i-1] {
			break
		} else if arr[i] == arr[i-1] {
			return false
		}
		i++
	}
	i--

	for j > 0 {
		if arr[j] > arr[j-1] {
			break
		} else if arr[j] == arr[j-1] {
			return false
		}
		j--
	}
	fmt.Println(i, j)
	return i == j && (len(arr) == 3 || (j != len(arr)-1 && i != 0))

}
func main() {
	var arr = []int{0, 3, 2, 1}
	fmt.Println(validMountainArray(arr))
}
