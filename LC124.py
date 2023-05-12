# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            cur = node.val + l + r
            ans = max(ans, cur)
            return node.val + max(l, r)
        dfs(root)
        return ans