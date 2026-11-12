class Solution:
    
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        peri = [0]
        n = len(grid)
        m = len(grid[0])
        def dfs(i,j):
            if i < 0 or i >= n or j < 0  or j >= m  or  grid[i][j] == 0:
                peri[0] += 1
                return 
            if grid[i][j] == -1:
                return
            grid[i][j] = -1
            dfs(i + 1,j)
            dfs(i ,j + 1)
            dfs(i-1,j)
            dfs(i,j -1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return peri[0]
        return -1