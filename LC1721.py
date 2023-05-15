# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        dummy = ListNode(0)
        cur = dummy
        
        for i in arr:
            node = ListNode(i)
            cur.next = node
            cur = cur.next

        return dummy.next