class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = []
        for n in num:
            while arr and k and arr[-1] > n:
                arr.pop()
                k -= 1
            if arr or n is not '0':
                arr.append(n)

        if k:
            arr = arr[0:-k]
        
        return ''.join(arr) or '0'