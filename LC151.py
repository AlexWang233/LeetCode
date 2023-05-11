class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        temp = ""
        for c in s:
            if c == " ":
                if temp == "":
                    continue

                if len(ans) > 0:
                    ans = " " + ans
                ans = temp + ans
                temp = ""

            else:
                temp += c

        if len(temp) > 0:
            if len(ans) > 0:
                ans = " " + ans
            ans = temp + ans
        return ans