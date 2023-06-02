"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def checkLeaf(self, g) -> bool:
        item = g[0][0]
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j] != item:
                    return False
        return True
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        if self.checkLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        n = len(grid)
        return Node(True, False, 
                    self.construct([row[:n//2] for row in grid[:n//2]]),
                    self.construct([row[n//2:] for row in grid[:n//2]]),
                    self.construct([row[:n//2] for row in grid[n//2:]]),
                    self.construct([row[n//2:] for row in grid[n//2:]]))