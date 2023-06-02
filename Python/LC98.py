# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateBST(root: Optional[TreeNode], low: int, high: int) -> bool:
            if not root:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            return validateBST(root.left, low, root.val) and validateBST(root.right, root.val, high)
        
        return validateBST(root, float('-inf'), float('inf'))