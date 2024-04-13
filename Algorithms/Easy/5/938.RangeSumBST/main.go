package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func bst(node *TreeNode, res *int, l int, r int) {

	if node.Left != nil {
		if node.Val > l {
			bst(node.Left, res, l, r)
		}
	}
	fmt.Println(l, node.Val, r, l <= node.Val && node.Val <= r)
	if l <= node.Val && node.Val <= r {
		*res += node.Val
	}
	if node.Right != nil {
		if node.Val < r {
			bst(node.Right, res, l, r)
		}
	}

}

func rangeSumBST(root *TreeNode, low int, high int) int {
	var res int
	bst(root, &res, low, high)
	return res
}

func main() {
	l := TreeNode{2, nil, nil}
	root := TreeNode{100, &l, nil}
	// fmt.Println(root)
	rangeSumBST(&root, 1, 1)
	// fmt.Println(root)
}
