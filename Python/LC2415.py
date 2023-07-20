# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk = deque([root])
        isOdd = False
        while stk:
            if isOdd:
                l = 0
                r = len(stk) - 1
                while l < r:
                    stk[l].val, stk[r].val = stk[r].val, stk[l].val
                    l += 1
                    r -= 1
            if not stk[0].left:
                break
            for _ in range(len(stk)):
                cur = stk.popleft()
                stk.append(cur.left)
                stk.append(cur.right)
            isOdd = not isOdd
        return root
