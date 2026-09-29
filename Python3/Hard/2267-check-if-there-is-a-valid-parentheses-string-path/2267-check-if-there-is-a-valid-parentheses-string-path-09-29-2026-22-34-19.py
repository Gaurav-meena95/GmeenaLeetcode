class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        dp = [[]]
        m ,n = len(grid),len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        maxOpen = (m + n) // 2
        dp =[[[-1] * (maxOpen + 1) for i in range(n)] for i in range(m)]

        def fn(i ,j,openCount):
            if grid[i][j] == '(':
                openCount += 1
            else:
                openCount -= 1
            if openCount < 0 or openCount > maxOpen:
                return False
            
            if i == m - 1  and j == n - 1 :
                return openCount == 0
            if dp[i][j][openCount] != -1:
                return dp[i][j][openCount] == 1
            res = False
            if i + 1 < m and fn(i + 1,j,openCount):
                    res =  True
            if j + 1 < n and fn(i,j + 1,openCount):
                    res =  True
            dp[i][j][openCount] = 1 if res else 0
            return res
        return fn(0,0,0)
