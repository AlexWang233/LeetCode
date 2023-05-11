class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        arr = list(s)
        while start < end:
            if arr[start] in vowels and arr[end] in vowels:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            while start < len(s) and arr[start] not in vowels:
                start += 1
            while end >= 0 and arr[end] not in vowels:
                end -= 1

        return ''.join(arr)