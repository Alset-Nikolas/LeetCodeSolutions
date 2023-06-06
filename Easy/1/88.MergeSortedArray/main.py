def var_1(nums1, m, nums2, n):
    l = 0
    r = 0
    arr = [0]*(n+m)
    i = 0
    while l < m and r<n:
        if nums1[l] < nums2[r]:
            arr[i] = nums1[l]
            l+= 1
        else:
            arr[i] = nums2[r]
            r += 1
        i += 1
    for index, a, len_ in [(l, nums1, m), (r,nums2,n)]:
        while index < len_:
            arr[i] = a[index]
            index+= 1
            i += 1
    for i, x in enumerate(arr):
        nums1[i] = x
    return nums1

def var_2(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if i >=0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        return var_1(nums1, m, nums2, n)
        # return var_2(nums1, m, nums2, n)


if __name__ == "__main__":
    s = Solution()
    assert s.merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6]
