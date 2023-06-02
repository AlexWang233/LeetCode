class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        i = j = d = 0
        m = 0
        def updateD(d: int) -> int:
            d += 1
            d %= 4
            return d
        for k in range(n * n):
            A[i][j] = k + 1
            match d:
                case 0:
                    j += 1
                    if j + 1 >= n or A[i][j+1] != 0:
                        d = updateD(d)
                case 1:
                    i += 1
                    if i + 1 >= n or A[i+1][j] != 0:
                        d = updateD(d)
                case 2:
                    j -= 1
                    if j == 0 or A[i][j-1] != 0:
                        d = updateD(d)
                case 3:
                    i -= 1
                    if i == 0 or A[i-1][j] != 0:
                        d = updateD(d)

        return A
                