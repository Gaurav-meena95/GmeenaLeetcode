class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        mx = curr_sum
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            mx = max(mx, curr_sum)
        return mx / k