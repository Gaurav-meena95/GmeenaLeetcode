class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(r,c):
            if r >= n or r < 0 or c >= m or c < 0:
                return False
            if grid[r][c] == 1:
                return True
            grid[r][c] = 1
            left = dfs(r-1,c)
            right = dfs(r+ 1,c)
            up = dfs(r,c-1)
            down = dfs(r,c + 1)
            return left and right and up and down

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    if dfs(i,j):
                        ans += 1
        return ans