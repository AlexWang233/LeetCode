class Solution:
    def knightDialer(self, n: int) -> int:
        cur = [1] * 10
        mod = 10 ** 9 + 7
        adjList = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        for i in range(n - 1):
            temp = [0] * 10
            for ind, occ in enumerate(cur):
                for adj in adjList[ind]:
                    temp[adj] += occ
            for j in range(10):
                cur[j] = temp[j] % mod

        return sum(cur) % mod