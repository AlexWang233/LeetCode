class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        maxSum = -float("inf")
        maxSumTemp = 0
        
        for i in nums:
            maxSumTemp += i            
            if maxSumTemp > maxSum:
                maxSum = maxSumTemp
            
            if maxSumTemp < 0:
                maxSumTemp = 0
        
        minSum = -float("inf")
        minSumTemp = 0      
        
        for i in nums:
            minSumTemp += -i            
            if minSumTemp > minSum:
                minSum = minSumTemp
            
            if minSumTemp < 0:
                minSumTemp = 0
                
        maxSumCircular = sum(nums) + (minSum)
        
        if sum(nums) == -minSum:
            return maxSum
        return max(maxSum,maxSumCircular)