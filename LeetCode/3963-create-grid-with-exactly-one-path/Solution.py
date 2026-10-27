class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#']*n for _ in range(m)]
        def fn(i,j):
            if i >= m  or j >= n:
                return False
            grid[i][j] = '.'
            if i == m-1 and j == n-1:
                return True
            if fn(i+1,j):
                return True
            if fn(i,j+1):
                return True
        fn(0,0)
        return [''.join(r) for r in grid]