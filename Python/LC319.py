class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Idea is that bulb is on iff it has odd number of factors, which are perfect squares
        return int(n ** 0.5)