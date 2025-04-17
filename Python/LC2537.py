class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        n = len(nums)
        left = 0
        c = res = 0
        for right in range(n):
            c += d[nums[right]]
            d[nums[right]] += 1
            while c >= k:
                res += n - right
                d[nums[left]] -= 1
                c -= d[nums[left]]
                left += 1
        return res