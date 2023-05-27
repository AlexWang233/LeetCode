class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        have, trie, self.res = set(), {}, []
        
        for i in range(m):
            for j in range(1, n):
                have.add(board[i][j] + board[i][j-1])
        for i in range(1, m):
            for j in range(n):
                have.add(board[i][j] + board[i-1][j])
        
        for w in words:
            for i in range(len(w)-1):
                a, b = w[i], w[i+1]
                if a+b not in have and b+a not in have: break
                else:
                    node = trie
                    for c in w:
                        if c not in node: node[c] = {}
                        node = node[c]
                    node['*'] = w
        
        def dfs(i, j, node):
            node = node[board[i][j]]
            if '*' in node:
                self.res.append(node['*'])
                del node['*']
            
            tmp, board[i][j] = board[i][j], '*'
            for x, y in (0, 1), (0, -1), (1, 0), (-1, 0):
                I, J = i+x, j+y
                if not (0 <= I < m and 0 <= J < n and board[I][J] in node): continue
                dfs(I, J, node)
                if len(node[board[I][J]]) == 0: del node[board[I][J]]
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return self.res