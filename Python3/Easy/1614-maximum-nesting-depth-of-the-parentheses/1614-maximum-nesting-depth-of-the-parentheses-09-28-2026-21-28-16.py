class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        count = 0
        for i in s:
            if i == '(':
                count += 1
            if i == ')':
                ans = max(ans,count)
                count -= 1
        return ans

