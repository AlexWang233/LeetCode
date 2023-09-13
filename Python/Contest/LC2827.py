class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:


        @cache
        def dp(i, flag, rest, odd_even):
            if i == len(t):
                return flag >= 0 and rest == odd_even == 0
            ans = 1 if 0 < i < len(t) and rest == odd_even == 0 else 0
            start = 1 if i == 0 else 0
            for j in range(start, 10):
                new_flag = flag
                if flag == 0:
                    if j > int(t[i]):
                        new_flag = -1
                    if j < int(t[i]):
                        new_flag = 1

                if j % 2:
                    ans += dp(i + 1, new_flag, (rest * 10 + j) % k, odd_even + 1)
                else:
                    ans += dp(i + 1, new_flag, (rest * 10 + j) % k, odd_even - 1)
            return ans
        
        t = str(high)
        high = dp(0, 0, 0, 0)
        dp.cache_clear()
        t = str(low - 1)
        low = dp(0, 0, 0, 0)
        return high - low
                