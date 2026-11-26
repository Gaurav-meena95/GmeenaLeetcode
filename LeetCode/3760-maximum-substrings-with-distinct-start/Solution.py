class Solution:
    def maxDistinct(self, s: str) -> int:
        p = set()
        for i in s:
            p.add(i)
        return len(p)