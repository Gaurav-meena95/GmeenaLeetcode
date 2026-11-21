class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        child = [[] for _ in s]
        for x in range(1, len(s)):
            child[parent[x]].append(x)
        size, last = [1] * len(s), {}  

        def dfs(x: int) -> None:
            c = s[x]
            above = last.get(c, -1)  
            last[c] = x
            for i in child[x]:
                dfs(i)
            last[c] = above
            if x:  
                size[above if above >= 0 else parent[x]] += size[x]

        dfs(0)
        return size