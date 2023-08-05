class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        cur = 0
        q = deque([])
        for n in nums:
            q2 = deque([])
            cur = n
            while len(q) > 0:
                val, count = q.pop()
                cur -= val
                if count > 1:
                    q2.append((val, count - 1))
            if cur < 0:
                return False
            elif cur > 0:
                q2.append((cur, k-1))
            q = q2
        
        return len(q) == 0