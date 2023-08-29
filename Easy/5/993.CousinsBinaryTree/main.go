package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func bst(node *TreeNode, x int, h int) (int, *TreeNode) {
	// return h node
	if node.Val == x {
		return h, nil
	}
	hx := -1
	var p *TreeNode = nil
	if node.Left != nil {
		if node.Left.Val == x {
			return h + 1, node
		} else {
			hx, p = bst(node.Left, x, h+1)
		}
	}
	if node.Right != nil && hx != -1 {
		if node.Right.Val == x {
			return h + 1, node
		} else {
			hx, p = bst(node.Right, x, h+1)
		}
	}
	return hx, p
}

func isCousins(root *TreeNode, x int, y int) bool {
	hx, px := bst(root, x, 0)
	hy, py := bst(root.Right, y, 0)
	if px == py {
		return false
	}
	return hx == hy

}

func main() {
	var mass = []int{-3, -2, -1, 0, 0, 0, 1, 2, 3}
	fmt.Println(isCousins(mass, 2))

}
