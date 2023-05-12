# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return cur