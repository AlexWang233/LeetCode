# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = [root]
        ans = 0
        while q:
            node = q.pop()
            n = node.val
            if low <= n <= high:
                ans += n
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans
