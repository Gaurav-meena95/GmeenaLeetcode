class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        d = 0
        for i in seq:
            if i  == '(':
                d += 1
            if d % 2 == 0:
                ans.append(1)
            else:
                ans.append(0)
            if i == ')':
                d -= 1
        return ans
