class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:

        ans = set()
        cur = set()

        for i in arr:
            nxt = {j | i for j in cur}
            nxt.add(i)
            ans.update(nxt)
            cur = nxt

        return len(ans)