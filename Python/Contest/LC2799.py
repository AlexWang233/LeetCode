class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n,  k = len(nums), len(set(nums))
        res = start = 0
        count = Counter()
        for end in range(n):
            count[nums[end]] += 1
            while len(count) == k:
                count[nums[start]] -= 1
                if count[nums[start]] == 0:
                    del count[nums[start]]
                start += 1
            res += start
        return res