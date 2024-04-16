# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return None
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        if depth == 2:
            n1 = TreeNode(val)
            n1.left = root.left
            n2 = TreeNode(val)
            n2.right = root.right
            root.left = n1
            root.right = n2
            return root
        root.left = self.addOneRow(root.left, val, depth - 1)
        root.right = self.addOneRow(root.right, val, depth - 1)
        return root