class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s = sum(nums)
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            if presum == s:
                return i
            s -= nums[i]
        return -1