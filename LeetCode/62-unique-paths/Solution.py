class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def fn(i,j):
            if i >= m