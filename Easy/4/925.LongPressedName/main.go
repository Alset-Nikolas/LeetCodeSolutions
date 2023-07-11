package main

import (
	"fmt"
)

func isLongPressedName(name string, typed string) bool {
	// flag := true
	n, m := 0, 0
	j_start := 0
	last_j := 0
	var last_symvol byte = name[0]
	for i := 0; i < len(name); i++ {
		if name[i] == last_symvol {
			n++
		} else {
			m = 0
			for j := j_start; j < len(typed); j++ {
				if typed[j] != last_symvol {
					j_start = j
					break
				}
				m++
				last_j = j

			}
			if n > m {
				return false
			}
			last_symvol = name[i]
			n = 1

		}

	}
	if n > 0 {
		m = 0
		for j := j_start; j < len(typed); j++ {
			if typed[j] != last_symvol {
				j_start = j
				break
			}
			m++
			last_j = j

		}

		if n > m {
			return false
		}
	}
	return last_j == len(typed)-1
}

func main() {
	var name, typed string = "saeed", "ssaaedd"

	res := isLongPressedName(
		name,
		typed,
	)

	fmt.Println(res)
}
