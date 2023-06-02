class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        l = len(isConnected)

        def findProvince(i: int) -> None:
            for j in range(l):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = isConnected[j][i] = 0
                    findProvince(j)

        for i in range(l):
            if isConnected[i][i]:
                ans += 1
                findProvince(i)

        return ans