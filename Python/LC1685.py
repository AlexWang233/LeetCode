class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        prefix_sum[0] = nums[0]
        suffix_sum[-1] = nums[n - 1]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[-i-1] = suffix_sum[- i] + nums[-i-1]

        for i in range(n):
            cur = ((nums[i] * i) - prefix_sum[i]) + (suffix_sum[i] - (nums[i] * (n - i - 1)))
            result[i] = cur

        return result