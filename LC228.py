class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        l = len(nums)
        i = 0
        while i < l:
            n = nums[i]
            j = i
            while j + 1 < l and nums[j + 1] == nums[j] + 1:
                j += 1
            if j > i:
                ans.append(str(nums[i])+"->"+str(nums[j]))
            else:
                ans.append(str(nums[i]))
            i = j + 1
        return ans
