class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        l = len(nums)
        while low < high:
            mid = (low + high) // 2
            i = j = 0
            while i < l - 1:
                if nums[i + 1] - nums[i] <= mid:
                    j += 1
                    i += 1
                i += 1
            if j >= p:
                high = mid
            else:
                low = mid + 1
        return low 