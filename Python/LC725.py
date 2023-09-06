# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k
        l = 0
        node = head
        while node:
            l += 1
            node = node.next

        n, m = divmod(l, k)
        node, prev = head, None

        for i in range(k):
            res[i] = node
            for j in range(n):
                prev = node
                node = node.next
            
            if m > 0:
                prev = node
                node = node.next
                m -= 1
            
            if prev:
                prev.next = None

        return res

            
