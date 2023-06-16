class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def findSubsets(ind: int, arr = List[int]):
            if ind == l:
                ans.append(arr)
                return
            findSubsets(ind + 1, arr)
            findSubsets(ind + 1, arr + [nums[ind]])

        ans = []
        l = len(nums)
        findSubsets(0, [])
        return ans