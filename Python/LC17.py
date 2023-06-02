class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        k = digits[0]
        l = len(digits)
        ans = [dic[k][i] for i in range(len(dic[k]))]
        for i in range(1, l):
            l2 = len(ans)
            for j in range(l2):
                s = dic[digits[i]]
                l3 = len(s)
                for k in range(l3 - 1):
                    ans.append(ans[j] + dic[digits[i]][k])
                ans[j] += dic[digits[i]][l3 - 1]

        return ans
