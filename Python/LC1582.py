class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        r = list(map(lambda x: sum(x) == 1, mat))
        c = list(map(lambda x: sum(x) == 1, zip(*mat)))
        print(r, c)

        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and r[i] and c[j]:
                    res += 1

        return res