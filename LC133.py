"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        q = deque([node])
        clone = {node.val: Node(node.val, [])}

        while q:
            cur = q.popleft()
            c = clone[cur.val]

            for n in cur.neighbors:
                if n.val not in clone:
                    clone[n.val] = Node(n.val, [])
                    q.append(n)
                c.neighbors.append(clone[n.val])

        return clone[node.val]