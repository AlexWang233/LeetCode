# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        res = []
        for i in range(2, n, 2):
            left_comb = self.allPossibleFBT(i - 1)
            right_comb = self.allPossibleFBT(n - i)
            for left_child in left_comb:
                for right_child in right_comb:
                    tree = TreeNode(0, left_child, right_child)
                    res.append(tree)
        return res