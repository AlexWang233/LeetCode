class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        l = len(nums) - 1
        if l < 0:
            return [-1, -1]
        start, end = 0, l
        mid = 0
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                break
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1

        mid = (start + end) // 2
        if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
            first = mid
        
        start, end = first, l
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target and (mid == l or nums[mid + 1] > target):
                break
            if nums[mid] > target:
                end = mid
            else:
                start = mid + 1

        mid = (start + end) // 2
        if nums[mid] == target and (mid == l or nums[mid + 1] > target):
            last = mid

        return [first, last]
                