class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        children = set(leftChild + rightChild)

        for i in range(n):
            if i not in children:
                root = i
                break

        visited = set()
        q = deque([root])

        while q:
            node = q.popleft()
            if node in visited:
                return False

            visited.add(node)

            if leftChild[node] != -1:
                q.append(leftChild[node])
            if rightChild[node] != -1:
                q.append(rightChild[node])

        return len(visited) == n
        