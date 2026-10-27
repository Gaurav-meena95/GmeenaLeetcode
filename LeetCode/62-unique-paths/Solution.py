class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        def fn(i,j):
            if i >= m or j >= n:
                return False
            fn(i + 1, j)
            fn()