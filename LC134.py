class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = cur = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            cur += (gas[i] - cost[i])
            if cur < 0:
                cur = 0
                start = i + 1
        if total < 0:
            return -1
        return start