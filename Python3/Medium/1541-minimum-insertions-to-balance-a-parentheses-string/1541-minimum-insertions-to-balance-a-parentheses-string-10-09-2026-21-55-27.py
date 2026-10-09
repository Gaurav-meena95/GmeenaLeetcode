class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                stack.append('(')
                i += 1
            elif s[i] == ')' and (i + 1 < n and s[i + 1] == ')'):
                if not stack:
                    ans += 1
                else:
                    stack.pop()
                i += 2
            else :
                if not stack:
                    ans += 2
                else:
                    stack.pop()
                    ans += 1
                i += 1
        ans += len(stack) * 2
        return ans

        