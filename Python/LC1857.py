class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        l = len(colors)
        inArc = [0] * l
        outArc = [[] for i in range(l)]
        for u, v in edges:
            inArc[v] += 1
            outArc[u].append(v)

        stack = [u for u in range(l) if inArc[u] == 0]
        colorCount = [[0]*26 for i in range(l)]

        while stack:
            u = stack.pop()
            colorCount[u][ord(colors[u]) - ord('a')] += 1
            for v in outArc[u]:
                colorCount[v] = [max(colorCount[u][i], colorCount[v][i]) for i in range(26)]
                inArc[v] -= 1
                if inArc[v] == 0:
                    stack.append(v)

        if any(inArc):
            return -1
        
        return max([max(node) for node in colorCount])