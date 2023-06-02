# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(lower, upper):
            if lower == upper:
                return [None]
            trees = []
            for i in range(lower, upper):
                for l in generate(lower, i):
                    for r in generate(i+1, upper):
                        node = TreeNode(i+1, l, r)
                        trees.append(node)
            return trees
        return generate(0, n)