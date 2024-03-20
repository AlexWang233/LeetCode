# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = ListNode(0)
        head.next = list1
        i = 1
        cur = list1
        while i < a:
            cur = cur.next
            i += 1
        
        node = list2
        while node.next:
            node = node.next
        
        cur2 = cur
        while i <= b:
            cur2 = cur2.next
            i += 1
        
        node.next = cur2.next
        cur.next = list2

        return head.next