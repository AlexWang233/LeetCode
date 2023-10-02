class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = b = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1] == 'A':
                a += 1
            elif colors[i - 1] == colors[i] == colors[i + 1] == 'B':
                b += 1
        return a > b
            
            