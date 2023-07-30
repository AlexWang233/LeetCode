class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = mainTank
        newDist = mainTank
        while newDist >= 5:
            additional = min(newDist // 5, additionalTank)
            newDist = newDist % 5 + additional
            additionalTank -= additional
            res += additional
        return res * 10
            