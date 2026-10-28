class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [set() for _ in range(m)]
        dp[0].add(grid[0][0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                if j > 0:
                    reach =dp[j] | dp[j - 1]
                else:
                    reach = dp[j]
                dp[j] = {k ^ val for k in reach}
        return min(dp[-1])