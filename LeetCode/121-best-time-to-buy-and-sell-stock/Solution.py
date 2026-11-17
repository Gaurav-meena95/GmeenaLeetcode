class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_p = float('inf')
        ans = 0
        for i in prices:
            min_p = min(min_p , i )
            ans = max(ans,i - min_p)
        return ans