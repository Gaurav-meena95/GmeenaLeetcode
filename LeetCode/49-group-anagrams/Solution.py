class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = {}
        
        for i in strs:
            key = "".join(sorted(i))
            
            if key not in ans:
                ans[key] = []
            ans[key].append(i)
            
        return list(ans.values())