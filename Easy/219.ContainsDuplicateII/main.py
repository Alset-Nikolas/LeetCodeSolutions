from typing import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = set()
        k += 1
        for i in range(len(nums)):
            x = nums[i]
            if len(numbers) >= k:
                numbers.remove(nums[i-k])
            if x not in numbers:
                numbers.add(x)
            else:
                return True
        return False
    
if __name__ == "__main__":
    s = Solution()
    assert s.containsNearbyDuplicate([1,2,3,1], 3)
    assert s.containsNearbyDuplicate([1,0,1,1], 1)
    assert not s.containsNearbyDuplicate([1,2,3,1,2,3], 2)


