# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        node.val += self.dfs(node.left) + self.dfs(node.right)
        return node.val

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        total = root.val
        ans = 0
        m = 10 ** 9 + 7
        arr = [root]
        while len(arr) > 0:
            temp = []
            for node in arr:
                ans = max(ans, (node.val) * (total - node.val))
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            arr = temp
        return ans % m

