class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = [asteroids[0]]
        for nex in asteroids[1:]:
            while stk:
                cur = stk.pop()
                if cur < 0 or nex > 0:
                    break
                if abs(cur) == abs(nex):
                    cur = 0
                    nex = 0
                    break
                elif abs(cur) > abs(nex):
                    nex = 0
                    break
                cur = 0
            if cur != 0:
                stk.append(cur)
            if nex != 0:
                stk.append(nex)
        return stk