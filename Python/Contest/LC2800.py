class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def mergeStr(s1, s2):
            if s2 in s1:
                return s1
            
            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return s1[:i] + s2
            return s1 + s2
        
        res, curMin = '', math.inf
        for s1, s2, s3 in permutations([a, b, c]):
            s = mergeStr(mergeStr(s1, s2), s3)
            if len(s) < curMin:
                res, curMin = s, len(s)
            elif len(s) == curMin:
                res = min(res, s)
        return res