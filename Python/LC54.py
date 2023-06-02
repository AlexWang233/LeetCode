class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        # Idea is to pop first row then rotate by 90 degrees
        return [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])