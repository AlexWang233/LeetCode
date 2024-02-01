class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        l = len(nums)
        if l % 3 > 0:
            return []

        nums.sort()

        res = []
        for i in range(0, l, 3):
            if nums[i + 2] - nums[i] <= k:
                res.append(nums[i : i + 3])
            else:
                return []

        return res