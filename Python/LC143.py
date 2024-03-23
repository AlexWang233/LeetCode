# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow.next
        while cur:
            node = cur.next
            cur.next = prev
            prev = cur
            cur = node
        slow.next = None

        h1, h2 = head, prev
        while h2:
            node = h1.next
            h1.next = h2
            h1 = h2
            h2 = node
        