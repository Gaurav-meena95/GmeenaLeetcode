class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m , n = len(grid),len(grid[0])
        dp = [[[-1]*2 for _ in range(n)] for _ in range(m) ]
        def fn(i,j,d):
            if i  == m - 1 and j == n -1:
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j][d] != -1:
                return dp[i][j][d]
            if grid[i][j] == 1:
                if d == 0: # move right 
                    dp[i][j][d] = fn(i + 1,j,1)
                else: # move down
                    dp[i][j][d] = fn(i , j + 1, 0)
            else:
                dp[i][j][d] =( fn(i + 1,j,1) + fn(i,j + 1,0))% mod
            return dp[i][j][d]
        return fn(0,0,0)