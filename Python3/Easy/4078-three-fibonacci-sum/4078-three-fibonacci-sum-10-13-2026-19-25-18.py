class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        prev1 = 0
        prev2 = 1
        curr = 1
        while prev1 + prev2 + curr <= n:
            if  prev1 + prev2 + curr == n:
                return True
            nxt = curr + prev2
            prev1 = prev2
            prev2 = curr
            curr = nxt
        return False
            
        