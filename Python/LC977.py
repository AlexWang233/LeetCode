class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        i, j = 0, len(nums) - 1
        for k in range(len(nums)-1, -1, -1):
            a = nums[i] * nums[i]
            b = nums[j] * nums[j]
            if a >= b:
                arr[k] = a
                i+=1
            else:
                arr[k] = b
                j-=1
        return arr