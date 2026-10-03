class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open1 = 0
        close1 = 0
        result1 = 0
        for i in s:
            if close1 > open1:
                open1 = 0
                close1 = 0
            if i == '(':
                open1 += 1
            else:
                close1 += 1
            if open1 == close1:
                result1 = max(result1,open1 + close1)

        open2 = 0
        close2 = 0
        result2 = 0
        for i in range(len(s)-1,-1,-1):
            if close2 < open2:
                open2 = 0
                close2 = 0
            if s[i] == ')':
                close2 += 1
            else:
                open2 += 1
            if open2  ==  close2:
                result2 = max(result2,open2 + close2)
        return max(result1 , result2)
        
        