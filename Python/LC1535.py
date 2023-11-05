class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)

        res = arr[0]
        count = 0
        for n in arr[1:]:
            if n < res:
                count += 1
            else:
                res = n
                count = 1
            if count >= k:
                return res

        return res
