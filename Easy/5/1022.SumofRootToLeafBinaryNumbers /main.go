package main

import "strconv"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func goTree(node TreeNode, pref string) int {
	res := 0
	pref = pref + strconv.FormatInt(int64(node.Val), 10)
	if node.Left == nil && node.Right == nil {
		val, _ := strconv.ParseInt(pref, 10, 64)
		return res + int(val)
	}
	if node.Left != nil {
		res += goTree(*node.Left, pref)
	}
	if node.Right != nil {
		res += goTree(*node.Right, pref)
	}
	return res

}

func sumRootToLeaf(root *TreeNode) int {
	return goTree(*root, "")
}
