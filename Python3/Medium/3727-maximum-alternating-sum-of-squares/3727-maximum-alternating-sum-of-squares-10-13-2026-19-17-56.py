class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        p = n // 2
        nums = sorted(abs(i) for i in nums)
        score = 0
        for i in range(n):
            if i < p:
                score += -1 * nums[i]**2
            else:
                score += nums[i]**2        
        return score