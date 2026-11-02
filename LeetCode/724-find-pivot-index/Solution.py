class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        s = sum(nums)
        presum = 0