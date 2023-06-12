class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        
        def dfs(i, j, isAtl):
            
            if isAtl:
                if (i, j) in atl: return
                atl.add((i, j))
                if i < len(heights) - 1 and heights[i+1][j] >= heights[i][j]:
                    dfs(i+1, j, True)
                if i > 0 and heights[i-1][j] >= heights[i][j]:
                    dfs(i-1, j, True)
                if j < len(heights[i]) - 1 and heights[i][j+1] >= heights[i][j]:
                    dfs(i, j+1, True)
                if j > 0 and heights[i][j-1] >= heights[i][j]:
                    dfs(i, j-1, True)
            else:
                if (i, j) in pac: return
                pac.add((i,j))
                if i < len(heights) - 1 and heights[i+1][j] >= heights[i][j]:
                    dfs(i+1, j, False)
                if i > 0 and heights[i-1][j] >= heights[i][j]:
                    dfs(i-1, j, False)
                if j < len(heights[0]) - 1 and heights[i][j+1] >= heights[i][j]:
                    dfs(i, j+1, False)
                if j > 0 and heights[i][j-1] >= heights[i][j]:
                    dfs(i, j-1, False)
                    
        for i in range(len(heights)):
            dfs(i, 0, True)
            dfs(i, len(heights[0]) - 1, False)
        for j in range(len(heights[0])):
            dfs(0, j, True)
            dfs(len(heights) - 1, j, False)

        return atl.intersection(pac)