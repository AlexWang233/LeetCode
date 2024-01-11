# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, cur_max, cur_min):
            if not node:
                return
            nonlocal res
            res = max(res, cur_max - node.val)
            res = max(res, node.val - cur_min)
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            dfs(node.left, cur_max, cur_min)
            dfs(node.right, cur_max, cur_min)
        dfs(root, root.val, root.val)
        return res