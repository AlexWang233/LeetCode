class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        MAX = 10 ** 5

        left = bisect_left(fruits, [startPos - k, 0])
        right = bisect_right(fruits, [startPos + k, MAX])
        fruits = fruits[left: right]

        mid = bisect_right(fruits, [startPos, 10 ** 5])
        init = 0
        if mid > 0 and fruits[mid - 1][0] == startPos:
            init = fruits[mid - 1][1]
            mid -= 1
            fruits.pop(mid)

        left = []
        cur = 0
        for i in range(mid - 1, -1, -1):
            cur += fruits[i][1]
            left.append([startPos - fruits[i][0], cur])

        right = []
        cur = 0
        for i in range(mid, len(fruits)):
            cur += fruits[i][1]
            right.append([fruits[i][0] - startPos, cur])

        ans = init
        idx = len(right)
        for dist, val in left:
            cur = val + init
            while idx > 0 and right[idx - 1][0] > k - 2 * dist:
                idx -= 1
            if idx > 0:
                cur += right[idx - 1][1]
            ans = max(ans, cur)

        idx = len(left)
        for dist, val in right:
            cur = val + init
            while idx > 0 and left[idx - 1][0] > k - 2 * dist:
                idx -= 1
            if idx > 0:
                cur += left[idx - 1][1]
            ans = max(ans, cur)

        return ans

        
