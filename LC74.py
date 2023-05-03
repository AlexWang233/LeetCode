class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1

        low, high = 0, m
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                return True
        row = high

        low, high = 0, n
        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row][mid] > target:
                high = mid - 1
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                return True
        return False