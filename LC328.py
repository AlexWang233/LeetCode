# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head

        if not head or not head.next:
            return odd

        even = head.next
        evenHead = even

        while odd.next and odd.next.next and even.next and even.next.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        if odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next

        even.next = None
        odd.next = evenHead

        return head



