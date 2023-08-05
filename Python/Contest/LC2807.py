# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        orig = head
        while node and node.next:
            n, m = node.val, node.next.val
            node2 = ListNode(math.gcd(n, m), node.next)
            node.next = node2
            node = node2.next
        return orig