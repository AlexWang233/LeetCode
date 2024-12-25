# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            nq = deque([])
            cur = -2 ** 31
            for node in q:
                if node.val > cur:
                    cur = node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            ans.append(cur)
            q = nq
        return ans
