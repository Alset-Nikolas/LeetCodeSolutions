package main

import (
	"fmt"
	"unicode/utf8"
)

func minInt(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func commonChars(words []string) []string {
	stats := make(map[string]int)
	flag := false
	for _, w := range words {
		var length = utf8.RuneCountInString(w)
		stats_w := make(map[string]int)
		for i := 0; i < length; i++ {
			w_i := string(w[i])
			_, val_exist := stats_w[w_i]
			if !val_exist {
				stats_w[w_i] = 1
			} else {
				stats_w[w_i]++
			}
		}
		if !flag {
			stats = stats_w
			flag = true
		} else {
			for key, val := range stats {
				val_2, val_exist := stats_w[key]
				if val_exist {
					stats[key] = minInt(val, val_2)

				} else {
					delete(stats, key)
				}
			}

		}
	}
	answer := []string{}
	for k, v := range stats {
		for i := 0; i < v; i++ {
			answer = append(answer, k)
		}
	}
	return answer

}

func main() {
	words := []string{"bella", "label", "roller"}
	fmt.Println(commonChars(words))

}
