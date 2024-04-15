# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def rec(node, isLeft):
            if not node:
                return 0
            if isLeft and not node.left and not node.right:
                return node.val
            return rec(node.left, True) + rec(node.right, False)
        return rec(root, False)