class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        visited = [False] * (l)
        visited[start] = True
        q = [start]
        while len(q) > 0:
            curLevel = []
            for i in q:
                if arr[i] == 0:
                    return True
                up = i + arr[i]
                if up < l and not visited[up]:
                    visited[up] = True
                    curLevel.append(up)
                down = i - arr[i]
                if 0 <= down and not visited[down]:
                    visited[down] = True
                    curLevel.append(down)
            q = curLevel

        return False