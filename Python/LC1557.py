class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Since graph is acyclic, we need only vertices that have 0 in-degree
        return list(set(range(n)) - set(j for i, j in edges))