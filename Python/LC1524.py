class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = odd = even = 0
        for n in arr:
            if n % 2 == 0:
                even += 1
            else:
                odd, even = even + 1, odd
            res += odd
            res %= (10 ** 9 + 7)
        return res