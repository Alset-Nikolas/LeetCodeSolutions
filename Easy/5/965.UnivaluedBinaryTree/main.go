package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(node *TreeNode, val int) bool {

	l := true
	r := true
	if node.Left != nil {
		l = dfs(node.Left, val)
	}
	if node.Right != nil {
		r = dfs(node.Right, val)
	}
	return node.Val != val && l && r
}

func isUnivalTree(root *TreeNode) bool {
	return dfs(root, root.Val)
}

// func main() {
// 	var s = []int{1, 2, 3, 3}
// 	fmt.Println(s)
// 	fmt.Println(isUnivalTree(s))
// }
