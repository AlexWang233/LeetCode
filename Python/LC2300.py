class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        s = spells.copy()
        spells.sort()
        potions.sort()
        l = len(potions)
        r = l - 1
        d = dict()
        for item in spells:
            if item in d:
                continue
            while item * potions[r] >= success and r >= 0:
                r -= 1
            d[item] = l - r - 1

        ans = []
        for item in s:
            ans.append(d[item])

        return ans