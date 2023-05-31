class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        start, end = 0, l
        mid = 0
        while start < end:
            mid = (start + end) // 2
            n = nums[mid]
            if target < nums[0] < n:
                start = mid + 1
            elif target >= nums[0] > n:
                end = mid
            elif n > target:
                end = mid
            elif n < target:
                start = mid + 1
            else:
                return mid


        if nums[mid] == target:
            return mid
        return -1
                    
