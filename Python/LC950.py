class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque()
        deck.sort(reverse=True)
        for c in deck:
            q.rotate()
            q.appendleft(c)
        return list(q)