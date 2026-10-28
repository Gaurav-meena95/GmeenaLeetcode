class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
        nums.sort()
        ans = 1
        curr = 1
        for i in range(len(nums)-1):
            diff = abs(nums[i] - nums[i + 1])
            if diff == 1:
                curr += 1 
            elif diff ==0:
                continue
            else:
                ans = max(curr,ans)
                curr = 1
        return max(curr,ans)