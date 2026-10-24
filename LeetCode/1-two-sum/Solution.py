class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [i,d[diff]]
            else:
                d[nums[i]] = i