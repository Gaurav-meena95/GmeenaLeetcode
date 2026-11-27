class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        copies = [0]*n
        chepest = float('inf')
        for i in range(n):
            chepest = min(chepest,items[i][1])
            for j in range(n):
                if i == j :
                    continue
                if items[j][0] % items[i][0] == 0:
                    copies[i] += 1
        dp = [[-1] * (budget + 1) for _ in range(n + 1)]
        def fn(chepest,n,budget):
            if n ==0 :
                return budget // chepest
            take = 0
            skip = 0
            if dp[n][budget] != -1:
                return dp[n][budget]
            if items[n-1][1] <= budget:
                take = 1 + copies[n-1] + fn(chepest,n-1,budget - items[n-1][1])
            skip = fn(chepest,n-1,budget)
            dp[n][budget] =  max(take,skip)
            return dp[n][budget]
        return fn(chepest,n,budget)