class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r, c = len(img), len(img[0])
        res = [[0] * c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                sum = 0
                count = 0
                for x in range(max(0, i - 1), min(r, i + 2)):
                    for y in range(max(0, j - 1), min(c, j + 2)):
                        sum += img[x][y]
                        count += 1
                res[i][j] = sum // count

        return res