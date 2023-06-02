class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque([(start, 0)])
        visited = {start}
        
        while q:
            node,steps = q.popleft()
            if node == end:
                return steps
            
            for c in "ACGT":
                for i in range(8):
                    n2 = node[:i] + c + node[i+1:]
                    if n2 not in visited and n2 in bank:
                        q.append((n2, steps+1))
                        visited.add(n2)
        return -1