class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # do tasks with max(start - actual) last
        tasks.sort(key = lambda x: x[1] - x[0])

        ans = 0
        for t in tasks:
            # increment by actual, or overwrite with start
            # ensures we've enough time to finish all prev tasks
            ans = max(ans + t[0], t[1])

        return ans
        