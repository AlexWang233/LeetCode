class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = len(nums)
        def atMostK(n):
            count = Counter()
            res = i = 0
            for j in range(l):
                if count[nums[j]] == 0:
                    n -= 1
                count[nums[j]] += 1
                while n < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        n += 1
                    i += 1
                res += j - i + 1
            return res
        ans = atMostK(k) - atMostK(k - 1)
        return ans