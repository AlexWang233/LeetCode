class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def findRoot(i):
            if root[i] == i:
                return i
            root[i] = findRoot(root[i])
            return root[i]

        def connectRoot(u, v):
            x, y = findRoot(u), findRoot(v)
            if x == y:
                return False
            root[y] = x
            return True

        def traverseEdge(t2):
            for t, u, v in edges:
                if t2 == t:
                    if connectRoot(u, v):
                        if t > 1:
                            self.e2 += 1
                        if t % 2 == 1:
                            self.e1 += 1
                    else:
                        self.ans += 1

        self.ans = 0
        self.e1 = 0
        self.e2 = 0

        root = [i for i in range(n + 1)]
        traverseEdge(3)

        bobRoot = root.copy()
        traverseEdge(1)

        root = bobRoot
        traverseEdge(2)

        if self.e1 == self.e2 == n - 1:
            return self.ans
        else:
            return -1




