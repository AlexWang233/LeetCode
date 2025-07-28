class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n

        l = len(nums)
        dp = {}

        def find_subsets(cur, idx) -> int:
            if idx == l:
                return 1 if cur == max_or else 0

            if (cur, idx) in dp:
                return dp[(cur, idx)]

            n1 = find_subsets(cur | nums[idx], idx + 1)

            n2 = find_subsets(cur, idx + 1)

            dp[(cur, idx)] = n1 + n2

            return dp[(cur, idx)]

        ans = find_subsets(0, 0)
        return ans