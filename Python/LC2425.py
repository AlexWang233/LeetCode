class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 0
        
        if n2 % 2 == 1:
            for i in nums1:
                ans ^= i

        if n1 % 2 == 1:
            for i in nums2:
                ans ^= i
        
        return ans