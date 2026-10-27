class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        posarr = []
        negarr = []
        ans = []
        for i in nums:
            if i > 0:
                posarr.append(i)
            else:
                negarr.append(i)
        i = 0
        j = 0
        while i < len(posarr) or j < len(negarr):
            ans.append(posarr[i])
            ans.append(negarr[j])
            i += 1
            j += 1
        
        while i < len(posarr):
            ans.append(posarr[i])
            i += 1
        while j < len(posarr):
            ans.append(posarr[j])
            j += 1
        return ans