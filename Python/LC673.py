class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        arr = []
        deck = []
        path = []
        
        for n in nums:
            deck_ind = bisect.bisect_left(arr, n)
            np = 1
            if deck_ind > 0:
                ind = bisect.bisect(deck[deck_ind - 1], -n)
                np = path[deck_ind - 1][-1] - path[deck_ind - 1][ind]

            if deck_ind == len(arr):
                arr.append(n)
                deck.append([-n])
                path.append([0, np])
            else:
                arr[deck_ind] = n
                deck[deck_ind].append(-n)
                path[deck_ind].append(np + path[deck_ind][-1])
                
        return path[-1][-1]