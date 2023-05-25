# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def pathSum(root: Optional[TreeNode], curSum) -> bool:
            if not root:
                return False
            curSum += root.val
            if not root.left and not root.right and curSum == targetSum:
                return True
            return pathSum(root.left, curSum) or pathSum(root.right, curSum)
        
        return pathSum(root, 0)