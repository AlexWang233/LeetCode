# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        stk2 = []
        node = l1
        while node:
            stk1.append(node.val)
            node = node.next
        node = l2
        while node:
            stk2.append(node.val)
            node = node.next

        prev = None
        cur = None
        carry = False
        while stk1 or stk2:
            n = 0
            if stk1:
                n += stk1.pop()
            
            if stk2:
                n+= stk2.pop()

            if carry:
                n += 1

            carry = (n >= 10)
            n %= 10
            prev = cur
            cur = ListNode(n)
            cur.next = prev

        if carry:
            prev = cur
            cur = ListNode(1)
            cur.next = prev
        return cur