class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        dp = [[]]
        m ,n = len(grid),len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        @cache
        def fn(i ,j,openCount):
            if grid[i][j] == '(':
                openCount += 1
            else:
                openCount -= 1
            if openCount < 0:
                return False
            
            if i == m - 1  and j == n - 1 :
                return openCount == 0
            if i + 1 < m and fn(i + 1,j,openCount):
                    return True
            if j + 1 < n and fn(i,j + 1,openCount):
                    return True
            return False
        return fn(0,0,0)
