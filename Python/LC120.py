class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        arr = triangle[0]
        for row in triangle[1:]:
            prevRow = arr.copy()
            for j in range(len(prevRow)):
                arr[j] = prevRow[j]+row[j]
                if j > 0:
                    arr[j] = min(arr[j], prevRow[j-1]+row[j])
            arr.append(prevRow[-1] + row[-1])
        
        return min(arr)