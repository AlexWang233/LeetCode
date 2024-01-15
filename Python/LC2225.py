class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = dict()
        ans0, ans1 = [], []
        for [winner, loser] in matches:
            d[winner] = d.get(winner, 0)
            d[loser] = d.get(loser, 0) + 1

        for player in d:
            if d[player] == 0:
                ans0.append(player)
            elif d[player] == 1:
                ans1.append(player)

        ans0.sort()
        ans1.sort()
        return [ans0, ans1]