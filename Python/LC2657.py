class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        arr = [False] * n
        count = 0
        ans = []
        for i in range(n):
            if arr[A[i] - 1]:
                count += 1
            arr[A[i] - 1] = True
            if arr[B[i] - 1]:
                count += 1
            arr[B[i] - 1] = True
            ans.append(count)

        return ans
