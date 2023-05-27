class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(arr: List[int], perm: List[int]):
            if not arr:
                ans.append(perm)
            for i in range(len(arr)):
                n = arr.pop(i)
                dfs(arr, perm + [n])
                arr.insert(i, n)
        dfs(nums,[])
        return ans