package main

func prefixesDivBy5(A []int) []bool {

	ans := []bool{}
	n := 0

	for _, v := range A {
		n = (n<<1 + v) % 5
		if n == 0 {
			ans = append(ans, true)
		} else {
			ans = append(ans, false)
		}
	}
	return ans
}
func main(){

}