class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sumn = 0
        ans = float('inf')
        left = 0
        for right in range(len(nums)):
            sumn += nums[right]
            while sumn >= target:
                ans = min(ans,right - left + 1)
                sumn -= nums[left]
                left += 1
        if ans == float('inf'):
            return 0
        return ans