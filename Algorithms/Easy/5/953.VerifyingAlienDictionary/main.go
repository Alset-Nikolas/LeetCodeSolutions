package main

func isAlienSorted(words []string, order string) bool {
	info := make(map[byte]int)
	for i := 0; i < len(order); i++ {
		info[order[i]] = i
	}
	for i := 1; i < len(words); i++ {
		w := words[i]
		w_last := words[i-1]
		j, k := 0, 0
		flag := false

		for j < len(w) && k < len(w_last) {
			if info[w[j]] > info[w_last[k]] {
				flag = true
				break
			} else if info[w[j]] < info[w_last[k]] {
				return false
			} else {
				j++
				k++
			}
		}
		if !flag && len(w) < len(w_last) {
			return false
		}

	}
	return true
}

// func main() {
// 	var s = []string{"cba", "daf", "ghi"}
// 	fmt.Println(s)
// }
