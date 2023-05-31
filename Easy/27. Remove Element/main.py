class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k =0 
        i =0
        last_x = None
        while i< len(nums):
            x = nums[i]
            if last_x is None:
                last_x = x
                k += 1
                i += 1
                continue
            if x != last_x:
                nums[k],nums[i] = nums[i], nums[k]
                last_x = x
                k += 1
            i += 1
        return k


if __name__ == "__main__":
    s = Solution()
  
    assert s.removeDuplicates([1,1,2]) == 2
    assert s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5