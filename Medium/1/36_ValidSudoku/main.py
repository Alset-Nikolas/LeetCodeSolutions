from typing import List


class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		boxs = [[set() for y in range(3)] for x in range(3)]
		clms = [set() for x in range(9)]
		lines = [set() for x in range(9)]
		for i, line in enumerate(board):
			for j, el in enumerate(line):
				if el == '.':
					continue
				el = int(el)
				if el > 9 or el < 0:
					return False
				if el in lines[i]:
					return False
				lines[i].add(el)
				if el in clms[j]:
					return False
				clms[j].add(el)
				i_3 = i // 3
				j_3 = j // 3
				if el in boxs[i_3][j_3]:
					return False
				boxs[i_3][j_3].add(el)
		return True

def run_tests():
	test1 =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
	assert Solution().isValidSudoku(test1) == True

if __name__ == "__main__":
	run_tests()
	items = list(map(int, input().split()))
	x = int(input())
	print(Solution().isValidSudoku(nums=items, target=x))
