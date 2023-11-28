class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        n = corridor.count('S')
        if n == 0 or n % 2 > 0:
            return 0

        i = 1
        count = 1 if corridor[0] == 'S' else 0
        res = 1
        while i < len(corridor):
            j = 1
            if count >= n - 2:
                break
            if corridor[i] == 'S':
                count += 1
                if count % 2 == 0:
                    while corridor[i + j] == 'P':
                        j += 1
                    res *= j
                    res %= mod
            i += j

        return res
