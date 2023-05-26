# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def countHeight(root: Optional[TreeNode]) -> int:
            if not root:
                return -1
            else:
                return 1 + countHeight(root.left)

        height = countHeight(root)
        if height == -1:
            return 0
        else:
            if countHeight(root.right) == height - 1:
                return (1 << height) + self.countNodes(root.right)
            else:
                return (1 << (height - 1)) + self.countNodes(root.left)