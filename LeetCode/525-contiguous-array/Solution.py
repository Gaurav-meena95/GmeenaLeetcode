class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        cursum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cursum -= 1
            if nums[i] == 1:
                cursum += 1
            if cursum in d:
                ans = max(ans,i - d[cursum])
            else:
                d[cursum] = i
        return ans