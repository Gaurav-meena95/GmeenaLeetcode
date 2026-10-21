class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if list(s) == sorted(s):
            return 0
        max_char = max(s)
        min_char = min(s)

        if n == 2:
            return -1
        if max_char == s[-1] or min_char == s[0]:
            return 1
        max_ch_mid = max(s[1:(n-1)])   
        min_ch_mid = min(s[1:(n-1)])    
        if s[0] > max_ch_mid and  s[-1] < min_ch_mid:
            return 3

        return 2
