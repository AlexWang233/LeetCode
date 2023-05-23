"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = defaultdict(lambda: Node(0))
        d[None] = None
        node = head
        while node:
            d[node].val = node.val
            d[node].next = d[node.next]
            d[node].random = d[node.random]
            node = node.next
        return d[head]