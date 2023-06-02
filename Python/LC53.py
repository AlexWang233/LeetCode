class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        temp = float('-inf')
        for num in nums:   
            if(temp + num <= num):
                temp = num 
            else: 
                temp += num
            if(temp > maximum):
                maximum = temp
        return maximum