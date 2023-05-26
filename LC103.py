# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        ans = []
        curLevel = [root]
        leftToRight = True
        while q or curLevel:
            if not q:
                if leftToRight:
                    cur = [node.val for node in curLevel]
                else:
                    cur = [node.val for node in curLevel[::-1]]
                ans.append(cur)
                leftToRight = not leftToRight
                q = curLevel.copy()
                curLevel = []
            
            node = q.pop(0)
            if node.left:
                curLevel.append(node.left)
            if node.right:
                curLevel.append(node.right)

        return ans
