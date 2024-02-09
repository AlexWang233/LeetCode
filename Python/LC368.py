class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
            s = {-1: set()}
            nums.sort()
            for n in nums:
                s[n] = max((s[d] for d in s if n % d == 0), key = len)
                s[n] = s[n] | {n} #s[n].add(n)
            res = list(max(s.values(), key = len))
            return res
            