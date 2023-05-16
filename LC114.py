# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        head = TreeNode(0)
        cur = head
        def flatten(node):
            nonlocal cur
            cur.left = None
            cur.right = node
            cur = cur.right
        def pre(node):
            if not node:
                return
            left = node.left
            right = node.right
            flatten(node)
            pre(left)
            pre(right)
        pre(root)