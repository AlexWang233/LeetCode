class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0, 0]
        for i in nums:
            if nums[abs(i) - 1] < 0:
                arr[0] = abs(i)
            else:
                nums[abs(i) - 1] *= -1
        for index, item in enumerate(nums):
            if item > 0:
                arr[1] = index+1
                break
        return arr