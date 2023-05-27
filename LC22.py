class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gp(left: int, right: int, s: str) -> None:
            if left > 0:
                gp(left - 1, right, s + "(")
            if right > left:
                gp(left, right - 1, s+")")
            if right == 0:
                ans.append(s)

        ans = []
        gp(n, n, "")
        return ans
