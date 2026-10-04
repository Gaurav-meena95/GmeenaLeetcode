class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1]*101 for i in range(101)]
        def fn(i,open):
            if open < 0:
                return False
            if i == n:
                return open == 0
            if dp[i][open] != -1:
                return dp[i][open]
            isvalid = False
            if s[i] == '*':
                a = fn(i + 1,open + 1)
                b = fn(i + 1,open)
                c = fn(i + 1,open - 1)
                isvalid =  a or b or c
            if s[i] == '(':
                isvalid =  fn(i + 1,open + 1)
            elif s[i] == ')':
                isvalid =  fn(i + 1,open - 1 )
            dp[i][open] = isvalid
            return dp[i][open]
            
        return fn(0,0)

        