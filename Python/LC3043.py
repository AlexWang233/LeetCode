class Solution:
    def digits(self, n):
        res = 0
        while n > 0:
            res += 1
            n //= 10
        return res

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()
        for n in arr1:
            cur = n
            while cur > 0:
                prefix_set.add(cur)
                cur //= 10

        ans = 0

        for n in arr2:
            cur = n
            cur_len = self.digits(cur)
            while cur > 0 and cur_len > ans:
                if cur in prefix_set:
                    ans = cur_len
                cur_len -= 1
                cur //= 10

        return ans
