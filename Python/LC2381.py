class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * n
        
        for l, r, t in shifts:
            if t == 1:
                arr[l] += 1
                if r + 1 < n:
                    arr[r + 1] -= 1
            else:
                arr[l] -= 1
                if r + 1 < n:
                    arr[r + 1] += 1
        
        for i in range(1, n):
            arr[i] += arr[i - 1]
        
        ans = []
        for i in range(n):
            shift = (arr[i] % 26 + 26) % 26 
            c = (ord(s[i]) - ord('a') + shift) % 26
            ans.append(chr(ord('a') + c))
        
        return ''.join(ans)