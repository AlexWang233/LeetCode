# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        @lru_cache
        def treeHeight(root):
            if not root:
                return 0
            return 1 + max(treeHeight(root.left), treeHeight(root.right))
        if not root:
            return 0
        return max([self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), treeHeight(root.left) + treeHeight(root.right)])