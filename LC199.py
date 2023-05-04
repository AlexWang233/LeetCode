# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def reachDepth(root: Optional[TreeNode], depth: int) -> None:
            if not root:
                return None
            if depth == len(ans):
                ans.append(root.val)
            reachDepth(root.right, depth + 1)
            reachDepth(root.left, depth + 1)
        ans = []
        reachDepth(root, 0)
        return ans
