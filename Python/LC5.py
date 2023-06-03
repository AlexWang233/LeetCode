class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 2 * len(s) + 3
        arr = [0]*l
        rad = [0]*l

        arr[0] = '#'
        arr[-1] = '@'
        c = 1
        for i in s:
            arr[c] = ' '
            c += 1
            arr[c] = i
            c += 1
        arr[c] = ' '

        maxLen = maxRight = start = center = 0

        for i in range(1, l - 1):
            if i < maxRight:
                rad[i] = min(maxRight - i, rad[center - i + center])

            while arr[i + rad[i] + 1] == arr[i - rad[i] - 1]:
                rad[i] += 1

            if i + rad[i] > maxRight:
                maxRight = i + rad[i]
                center = i

            if rad[i] > maxLen:
                maxLen = rad[i]
                start = (i - rad[i] - 1)//2

        return s[start:start+maxLen]