class Solution:
    def calPoints(self, operations: List[str]) -> int:
        q = []
        for i in operations:
            if i == '+':
                q.append(q[-1] + q[-2])
            elif i == 'D':
                q.append(q[-1] * 2)
            elif i == 'C':
                q.pop()
            else:
                q.append(int(i))
        return sum(q)