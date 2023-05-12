# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        d = defaultdict(lambda: 0)
        d[0] = 1
        self.ans = 0

        def dfs(node, curSum):
            if not node:
                return
            curSum += node.val
            target = curSum - targetSum
            self.ans += d[target]
            d[curSum] += 1
            dfs(node.left, curSum)
            dfs(node.right, curSum)
            d[curSum] -= 1

        dfs(root, 0)
        return self.ans