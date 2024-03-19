class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        max_freq = max(c.values())
        max_count = 0
        for v in c.values():
            if v == max_freq:
                max_count += 1

        ans = (max_freq - 1) * (n + 1) + max_count
        return max(ans, len(tasks))