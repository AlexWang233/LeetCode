# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk, l = [], []
        
        while True:
            while root:
                stk.append(root)
                root = root.left
                
            if not stk:
                return l
            
            node = stk.pop()
            l.append(node.val)
            root = node.right