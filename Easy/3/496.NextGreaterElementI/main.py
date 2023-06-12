from typing import * 
class Mystack:
    def __init__(self) -> None:
        self.mass = []

    def add(self, x):
        if self.is_empty():
            self.mass.append(x)
            return
        while not self.is_empty() and self.get_last() <= x:
            self.pop()
        self.mass.append(x)

    def get_last(self):
        return self.mass[-1]

    def is_empty(self):
        return self.mass == []
    
    def pop(self):
        return self.mass.pop()


    
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums2)
        my_stack = Mystack()
        info = dict()
        for i, x in enumerate(nums2[::-1]):
            my_stack.add(x)
            info[x] = -1
            if i ==0:
                continue
            for v in my_stack.mass[::-1]:
                if x < v:
                    ans[-i-1] = v
                    info[x] = v
                    break
        res = [-1]*len(nums1)
        for i, x in enumerate(nums1):
            if x in info:
                res[i] = info[x]
        print(res)
        
print(Solution().nextGreaterElement([2,4],[1,2,3,4]))
        
