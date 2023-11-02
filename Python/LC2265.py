# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            
            l_sum, l_count = dfs(node.left)
            r_sum, r_count = dfs(node.right)

            s = node.val + l_sum + r_sum
            c = 1 + l_count + r_count

            if s // c == node.val:
                res += 1

            return s, c

        dfs(root)

        return res