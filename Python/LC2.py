# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        l = ListNode(0)
        l3 = l
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n = n1 + n2
            if carry:
                n += 1
            carry = n // 10
            n = n % 10
            l.next = ListNode(n)
            l = l.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            l.next = ListNode(1)
        return l3.next
