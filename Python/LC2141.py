class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total_power = sum(batteries)
        # check whether the most powerful battery can last longer than every other battery combined
        while batteries[-1] > total_power / n:
            # if it does, disregard it and reduce number of computers
            # since we now assume that this battery powers it
            total_power -= batteries.pop()
            n -= 1
        # otherwise, we can reach a state where total battery power is < n
        # by using the batteries evenly (charge with batteries with most power each day)
        return total_power // n