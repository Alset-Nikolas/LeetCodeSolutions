package main

import (
	"fmt"
	"strings"
)

type Stack struct {
	mass []string
}

func NewStack() Stack {
	s := Stack{[]string{}}
	return s
}

func (s *Stack) add(x string) {
	if s.is_empty() {
		s.mass = append(s.mass, x)
		return
	}
	lastSimvol := s.pop()
	if lastSimvol == "(" && x == ")" {
		return
	}
	s.mass = append(s.mass, lastSimvol)
	s.mass = append(s.mass, x)

}
func (s *Stack) pop() string {
	x := s.mass[len(s.mass)-1]
	s.mass = s.mass[:len(s.mass)-1]
	return x
}
func (s *Stack) is_empty() bool {
	return len(s.mass) == 0
}

func removeOuterParentheses(s string) string {
	stack := NewStack()
	i := 0
	ans := []string{}
	for j, x := range s {
		stack.add(string(x))
		if stack.is_empty() {
			ans = append(ans, s[i+1:j])
			i = j + 1
		}
	}
	fmt.Println(ans)
	return strings.Join(ans, "")
}

func main() {
}
