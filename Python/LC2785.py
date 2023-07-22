class Solution:
    def sortVowels(self, s: str) -> str:
        iArr = []
        vArr = []
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for i, c in enumerate(s):
            if c in vowels:
                vArr.append(c)
                iArr.append(i)
        s = list(s)
        vArr.sort()
        count = 0
        for i in iArr:
            s[i] = vArr[count]
            count += 1
        return ''.join(s)
                
        