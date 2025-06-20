class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        mq = [0] * 4 # max of each quardrant
        x = y = 0
        d = [0] * 4
        ans = 0

        for c in s:
            if c == 'N':
                d[0] += 1
                y += 1
            elif c == 'S':
                d[1] += 1
                y -= 1
            elif c == 'E':
                d[2] += 1
                x += 1
            elif c == 'W':
                d[3] += 1
                x -= 1

            mq[0] = x + y + min(d[1] + d[3], k) * 2
            mq[1] = -x + y + min(d[1] + d[2], k) * 2
            mq[2] = -x - y + min(d[0] + d[2], k) * 2
            mq[3] = x - y + min(d[0] + d[3], k) * 2
            ans = max(ans, max(mq))

        return ans

