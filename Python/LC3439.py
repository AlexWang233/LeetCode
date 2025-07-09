class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        l = len(startTime)
        ans = 0
        prefix_sum = [0] * (l + 1)
        for i in range(l):
            prefix_sum[i + 1] = prefix_sum[i] + (endTime[i] - startTime[i])

        for i in range(k - 1, l):
            right = eventTime if i == l - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            t = right - left - prefix_sum[i + 1] + prefix_sum[i - k + 1]
            ans = max(ans, t)
            
        return ans
