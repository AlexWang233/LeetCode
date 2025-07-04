class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        def helper(i):
            res = 0
            j = 0
            while i > 0:
                if (i % 2) & (operations[j]):
                    res += 1
                j += 1
                i >>= 1
            return res

        ans = helper(k - 1) % 26
        return chr(ord('a') + ans)

        