class Solution:
    def isHappy(self, n: int) -> bool:
        ans = n
        visited = set()
        while True:
            temp = 0
            if ans == 1:
                return True
            while ans > 0:
                m = ans % 10
                temp += m*m
                ans = ans // 10
            if temp in visited:
                return False
            visited.add(temp)
            ans = temp