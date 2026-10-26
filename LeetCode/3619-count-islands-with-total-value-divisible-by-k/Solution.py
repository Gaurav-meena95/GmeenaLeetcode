class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or  grid[r][c] == 0:
                return 0
            s = grid[r][c]
            grid[r][c] = 0
            s += dfs(r + 1,c)
            s += dfs(r - 1,c)
            s += dfs(r ,c + 1)
            s += dfs(r,c - 1)
            return s
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if dfs(i,j) % k == 0:
                        ans += 1
        return ans