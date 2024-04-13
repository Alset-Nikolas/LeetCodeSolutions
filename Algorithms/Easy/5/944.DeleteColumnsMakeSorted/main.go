package main

import (
	"fmt"
)

func minDeletionSize(strs []string) int {
	errs := 0
	for i := 0; i < len(strs[0]); i++ {
		for j := 1; j < len(strs); j++ {

			if strs[j][i] < strs[j-1][i] {
				errs++
				break
			}
		}
	}
	return errs
}
func main() {
	var s = []string{"cba", "daf", "ghi"}
	fmt.Println(s)
	fmt.Println(minDeletionSize(s))
}
