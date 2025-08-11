class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = 10 ** 9 + 7
        arr = [1]
        i = 1
        while n > 0:
            j = n & -n
            n ^= j
            arr.append(j * arr[-1])
        ans = []
        for start, end in queries:
            ans.append(arr[end + 1] // arr[start] % m)
        return ans