class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return 1 if power >= tokens[0] else 0
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        cur = res = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                cur += 1
                res = max(res, cur)
                left += 1
            elif cur > 0:
                power += tokens[right]
                cur -= 1
                right -= 1
            else:
                break
        return res
            
