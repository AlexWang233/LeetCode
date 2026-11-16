class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            l = len(s)
            arr = []
            for i in range(0, l, k):
                cur = 0
                for j in range(i, min(i + k, l)):
                    cur += int(s[j])
                arr.append(str(cur))
            s = "".join(arr)
            # print(s)
        return s
