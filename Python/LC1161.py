# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        ans = 1
        curMax = -10**5
        l = 1
        while q:
            nextLevel = []
            cur = 0
            for node in q:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                cur += node.val
            if curMax < cur:
                curMax = cur
                ans = l
            l += 1
            q = nextLevel
        return ans