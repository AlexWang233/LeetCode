
from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        ps = {')':'(', ']':'[', '}':'{'}
        d = LifoQueue(len(s))
        for p in s:
            if p in (')', ']', '}'):
                if d.empty() or d.get() != ps[p]:
                    return False
            else:
                d.put(p)
        return d.empty()