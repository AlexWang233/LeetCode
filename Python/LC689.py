class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = 3
        ans = []
        for i in range(n):
            temp = []
            for j in range(i + 1):
                temp.append(j * k)
            ans.append(temp)

        curSum = []
        for i in range(n):
            curSum.append(sum(nums[i * k : (i + 1) *k]))

        bestSum = [0]
        for i in range(n):
            bestSum.append(bestSum[i] + curSum[i])
        
        startIndex = []
        for i in range(n):
            startIndex.append(i * k + 1)
        
        while startIndex[-1] <= len(nums) - k:
            for i in range(n):
                curSum[i] += (nums[startIndex[i] + k - 1] - nums[startIndex[i]- 1])

            for i in range(n):
                if curSum[i] + bestSum[i] > bestSum[i + 1]:
                    for j in range(i):
                        ans[i][j] = ans[i - 1][j]
                    ans[i][-1] = startIndex[i]
                    bestSum[i + 1] = curSum[i] + bestSum[i]
            
            for i in range(n):
                startIndex[i] += 1

        return ans[-1]
                


        