class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        res = []
        for n in s1:
            if n in s2:
                res.append(n)
        return res