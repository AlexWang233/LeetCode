class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        l = len(rooms)
        visited = [False] * l
        stk = set()
        stk.update(rooms[0])
        visited[0] = True
        while stk:
            r = stk.pop()
            if visited[r]:
                continue
            else:
                visited[r] = True
                stk.update(rooms[r])

        return all(visited)