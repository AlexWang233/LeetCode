class Solution:
	def shortestPathLength(self, graph: List[List[int]]) -> int:
		l = len(graph)
		ans = 0
		visited = []
		q = []  
		for i in range(l):
			visited.append(set([1<<i]))
			q.append([i,1<<i])
		while q:
			ans = ans + 1
			cur = []
			for node, val in q:
				for neigbour in graph[node]:
					mid_node = (1<<neigbour)|val
					if mid_node not in visited[neigbour]:
						if mid_node+1 == 1<<l:
							return ans
						visited[neigbour].add(mid_node)
						cur.append([neigbour, mid_node])
			q = cur

		return 0