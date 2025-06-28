class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [(n, i) for i, n in enumerate(nums)]
        arr.sort(key=lambda x: -x[0])
        top_k = sorted(arr[:k], key=lambda x: x[1])
        return [n for n, i in top_k]