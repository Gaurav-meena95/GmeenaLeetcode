class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d = {0:-1}
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            rem  = presum % k
            if rem in d:
                if i - d[rem] >= 2 :
                    return True
            else:
                d[rem] = i
        return False