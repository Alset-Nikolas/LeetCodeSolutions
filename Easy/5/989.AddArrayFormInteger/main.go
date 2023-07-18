package main

import (
	"fmt"
)

func reverseMass(mass []int) []int {
	for i := 0; i < len(mass); i++ {
		mass[i], mass[len(mass)-1-i] = mass[len(mass)-1-i], mass[i]
	}
	return mass
}

func addToArrayForm(num []int, k int) []int {
	mass := []int{}
	for i := len(num) - 1; i >= 0 || k > 0; {
		sum := 0
		if i >= 0 {
			sum += num[i]
			i--
		}
		sum += k % 10
		k /= 10
		mass = append(mass, sum%10)
		k += sum / 10

	}
	return reverseMass(mass)
}

func main() {
	var mass = []int{-3, -2, -1, 0, 0, 0, 1, 2, 3}
	fmt.Println(addToArrayForm(mass, 2))

}
