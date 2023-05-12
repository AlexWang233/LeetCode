class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = cur = -10**5
        ind = 0
        for i in range(len(nums)):
            if prev == cur == nums[i]:
                continue
            prev, cur = cur, nums[i]
            nums[ind] = nums[i]
            ind += 1
        return ind