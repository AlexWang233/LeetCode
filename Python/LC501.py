# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return
            d[node.val] += 1
            dfs(node.left)
            dfs(node.right)
            
        d = defaultdict(lambda: 0)
        dfs(root)

        mx = max(d.values())
        res = [key for key in d if d[key] == mx]
        return res
