class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers = deque(sorted(trainers))
        ans = 0

        for p in players:
            while trainers and trainers[0] < p:
                trainers.popleft()
            if trainers:
                ans += 1
                trainers.popleft()
            else:
                break

        return ans