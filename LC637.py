# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        level = [root]
        while level:
            cur = []
            t = 0
            c = 0
            for node in level:
                t += node.val
                c += 1
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            level = cur
            ans.append(t/c)
        return ans