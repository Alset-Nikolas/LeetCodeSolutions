package main

import "fmt"

type RecentCounter struct {
	items    []int
	n        int
	lastTime int
}

func Constructor() RecentCounter {
	return RecentCounter{
		items:    make([]int, 0),
		n:        0,
		lastTime: 0,
	}
}

func (this *RecentCounter) Ping(t int) int {
	if this.n == 0 {
		this.n++
		this.items = append(this.items, t)
		this.lastTime = t
		return 1
	}
	this.items = append(this.items, t)
	items := make([]int, 0, 0)
	for i := 0; i < len(this.items); i++ {
		if t-3000 <= this.items[i] {
			items = append(items, this.items[i])
		}
	}
	this.items = items
	this.n = len(this.items)
	this.lastTime = t
	return this.n
}

func main() {
	obj := Constructor()
	fmt.Print(obj)

}
