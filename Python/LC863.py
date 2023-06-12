# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # convert tree into a graph
        graph = collections.defaultdict(list)
        def dfs(parent, node):
            if parent and node:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            if node.left:
                dfs(node, node.left)
            if node.right:
                dfs(node, node.right)
        
        dfs(None, root)

        level = [target.val]
        visited = set(level)

        # find which nodes are distance k
        for _ in range(k):
            cur = []
            for u in level:
                for v in graph[u]:
                    if v not in visited:
                        cur.append(v)
            level = cur
            visited |= set(level)
        return level
                


            
            
