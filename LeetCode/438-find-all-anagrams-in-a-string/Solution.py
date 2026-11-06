from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        len_p = len(p)
        p_count = Counter(p)
        ans = []
        i = 0
        while i < n:
            if s[i] in p_count:
                sub = s[i : i + len_p]
                if Counter(sub) == p_count:
                    ans.append(i)
            i += 1
        return ans