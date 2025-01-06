class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        left = [0] * l
        count = 0
        for i in range(1, l):
            if boxes[i - 1] == '1':
                count += 1
            left[i] += left[i - 1] + count

        right = [0] * l
        count = 0
        for i in range(l - 2, -1, -1):
            if boxes[i + 1] == '1':
                count += 1
            right[i] += right[i + 1] + count

        ans = [left[i] + right[i] for i in range(l)]
        return ans