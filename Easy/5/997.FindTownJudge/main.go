package main

import (
	"fmt"
)

func findJudge(n int, trust [][]int) int {
	if n == 1 {
		if len(trust) == 0 {
			return 1
		}
		return -1
	}
	children := make(map[int]map[int]bool)
	parent := make(map[int]map[int]bool)
	res := -1
	for i := 0; i < len(trust); i++ {
		x, p := trust[i][0], trust[i][1]
		_, flag := children[p]
		if !flag {
			children[p] = make(map[int]bool)
		}
		children[p][x] = true
		_, flag2 := parent[x]
		if !flag2 {
			parent[x] = make(map[int]bool)
		}
		parent[x][p] = true
	}

	for p, chs := range children {
		_, flag := parent[p]
		if len(chs) == n-1 && !flag {
			if res != -1 {
				return -1
			}
			res = p
		}
	}
	fmt.Println(children)
	fmt.Println(parent)

	return res
}

func main() {
	var mass = [][]int{{1, 3}, {2, 3}}
	fmt.Println(mass, mass[0][1])
	fmt.Println(findJudge(3, mass))

}
