# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = ListNode(-5000, head)
        last = head
        cur = head.next

        while cur:
            if cur.val >= last.val:
                last = last.next
            else:
                prev = temp
                while prev.next.val <= cur.val:
                    prev = prev.next

                last.next = cur.next
                cur.next = prev.next
                prev.next = cur

            cur = last.next

        return temp.next
            