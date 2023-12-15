class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        start = set()
        end = set()

        for s, e in paths:
            start.add(s)
            end.add(e)

        res = (end - start).pop()
        return res
