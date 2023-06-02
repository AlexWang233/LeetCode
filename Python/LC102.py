# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        stk1 = []
        stk2 = [root]
        def evalNode(node: Optional[TreeNode]) -> int:
            return node.val
        
        while stk1 or stk2:
            if not stk1:
                ans.append(list(map(evalNode, stk2)))
                stk1 = stk2.copy()
                stk2 = []
            node = stk1.pop(0)
            if node.left:
                stk2.append(node.left)
            if node.right:
                stk2.append(node.right)
            
        return ans
            