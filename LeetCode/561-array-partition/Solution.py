class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sun = 0
        for i in range(0,len(nums),2):
            sun += nums[i]
        return sun