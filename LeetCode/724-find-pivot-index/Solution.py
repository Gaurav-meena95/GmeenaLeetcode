class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        sufix = [0] * n 
        sufix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            sufix[i] = sufix[i+1] + nums[i]
        for i in range(n):
            if sufix[i] - prefix[i] == 0:
                return i
        return -1