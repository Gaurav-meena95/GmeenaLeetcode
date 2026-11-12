class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            inc = 1
            j = i + 1
            while j < n and nums[j] > nums[j - 1]:
                inc += 1
                j += 1
            
            dec = 1
            j = i+ 1
            while j < n and nums[j] < nums[j - 1]:
                dec += 1
                j += 1
            ans = max(ans , inc,dec)
        return ans