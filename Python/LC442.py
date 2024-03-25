class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                res.append(abs(n))
            else:
                nums[i] *= -1
        return res