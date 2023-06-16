class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def traversal(nums):
            if len(nums) <= 1:
                return len(nums)
            leftTree = [x for x in nums if x < nums[0]]
            rightTree = [x for x in nums if x > nums[0]]
            leftComb = traversal(leftTree)
            rightComb = traversal(rightTree)
            if leftComb == 0:
                return rightComb
            if rightComb == 0:
                return leftComb
            res = comb(len(leftTree) + len(rightTree), len(leftTree))
            return res * leftComb * rightComb

        ans = traversal(nums) - 1
        return ans % (10 ** 9 + 7)