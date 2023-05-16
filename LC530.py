# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            arr.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        ans = 10**5
        for i in range(len(arr)-1):
            cur = abs(arr[i] - arr[i+1])
            ans = min(cur, ans)
        return ans