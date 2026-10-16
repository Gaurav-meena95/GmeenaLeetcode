class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1]*1001 for _ in range(1001)]
        def ispalindrome(i,j):
            if i >= j:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = ispalindrome(i + 1,j - 1)
                return dp[i][j]
            dp[i][j] = 0
            return dp[i][j]
            
        max_len = 0
        pos = -1
        for i in range(len(s)):
            for  j in range(i, len(s)):
                if ispalindrome(i,j):
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        pos = i
        return s[pos:pos+ max_len]
   

        