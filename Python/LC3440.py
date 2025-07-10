class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gap_forward = deque([0])
        prev_end = 0
        for i in range(n):
            gap = startTime[i] - prev_end
            gap_forward.append(max(gap_forward[-1], gap))
            prev_end = endTime[i]
        # print(gap_forward)

        gap_backward = deque([0])
        next_start = eventTime
        for i in range(n - 1, -1, -1):
            gap = next_start - endTime[i]
            gap_backward.appendleft(max(gap_backward[0], gap))
            next_start = startTime[i]
        # print(gap_backward)

        ans = 0
        for i in range(n):
            gap = max(gap_forward[i], gap_backward[i + 1])
            prev_end = 0 if i == 0 else endTime[i - 1]
            next_start = eventTime if i == n - 1 else startTime[i + 1]
            cur_interval = next_start - prev_end
            if gap < endTime[i] - startTime[i]:
                cur_interval -= (endTime[i] - startTime[i])
            ans = max(ans, cur_interval)
        
        return ans