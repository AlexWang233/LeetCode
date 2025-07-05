class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        c = Counter(arr)
        for key in c.keys():
            if key == c[key]:
                ans = max(ans, key)
        return ans