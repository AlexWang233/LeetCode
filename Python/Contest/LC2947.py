class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        l = len(s)
        vowelCount = [0]
        conCount = [0]
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for c in s:
            vowel, con = vowelCount[-1], conCount[-1]
            if c in vowels:
                vowel += 1
            else:
                con += 1
            vowelCount.append(vowel)
            conCount.append(con)
        res = 0
        for i in range(2, l+1):
            for j in range(i):
                vowelDiff = vowelCount[i] - vowelCount[j]
                conDiff = conCount[i] - conCount[j]
                if vowelDiff == conDiff and vowelDiff * conDiff % k == 0:
                    res += 1

        return res