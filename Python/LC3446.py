class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        def sortDiag(i: int, j: int, desc: bool) -> None:
            arr = []
            r, c = i, j
            while r < n and c < m:
                arr.append(grid[r][c])
                r += 1
                c += 1
            arr.sort(reverse = desc)
            #print(arr)
            for k in range(len(arr)):
                grid[i + k][j + k] = arr[k]

        for i in range(1, m):
            sortDiag(0, i, False)
        for j in range(n):
            sortDiag(j, 0, True)

        return grid