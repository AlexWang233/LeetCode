class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = 99
        t = ord(target)
        for l in letters:
            if ord(l) <= t:
                continue
            res = min(res, ord(l) - t)
        if res == 99:
            return letters[0]
        return chr(t + res)