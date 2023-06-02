class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        arr = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                arr[i] = arr[i - 1] + 1

        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                arr[i] = max(arr[i], arr[i + 1] + 1)

        return sum(arr)