class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        visited = {(0, 0)}

        for direction in path:
            if direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False