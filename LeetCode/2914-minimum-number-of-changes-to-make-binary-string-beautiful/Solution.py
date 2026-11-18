class Solution:
    def minChanges(self, s: str) -> int:
        prev = s[0]
        count = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == prev:
                count += 1
                continue
            if count % 2 == 0:
                count = 1
            else:
                count = 0
                ans += 1
            prev = s[i]
        return ans