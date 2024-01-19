class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        arr = matrix[0]
        for row in matrix[1:]:
            prevRow = arr.copy()
            for j in range(len(prevRow)):
                arr[j] = prevRow[j]+row[j]
                if j > 0:
                    arr[j] = min(arr[j], prevRow[j-1]+row[j])
                if j < len(prevRow) - 1:
                    arr[j] = min(arr[j], prevRow[j+1]+row[j])
        
        return min(arr)
