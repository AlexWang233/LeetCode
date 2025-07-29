class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * l

        BITS = 32
        latest = [-1] * BITS

        for i in range(l - 1, -1, -1):
            right_most = i

            for b in range(BITS):
                if (nums[i] >> b) & 1:
                    latest[b] = i

            right_most = max(right_most, max(latest))

            ans[i] = right_most - i + 1

        return ans