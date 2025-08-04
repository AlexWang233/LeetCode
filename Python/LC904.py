class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        r = 0
        ans = 0
        for i in range(len(fruits)):
            if i > 0:
                j = fruits[i - 1]
                d[j] -= 1
                if d[j] == 0:
                    d.pop(j)
                else:
                    continue
            while r < len(fruits) and (fruits[r] in d.keys() or len(d.keys()) < 2):
                d[fruits[r]] += 1
                r += 1

            ans = max(ans, sum(d.values()))
            if r == len(fruits):
                break

        return ans
            