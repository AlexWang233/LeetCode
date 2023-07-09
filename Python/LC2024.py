class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        res = 0
        d = defaultdict(lambda: 0)
        for i in range(len(answerKey)):
            d[answerKey[i]] += 1
            res = max(res, d[answerKey[i]])
            if i - left >= res + k:
                d[answerKey[left]] -= 1
                left += 1
        
        return len(answerKey) - left