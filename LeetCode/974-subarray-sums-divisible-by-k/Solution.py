class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        d = {0:1}
        ans = 0
        presum = 0
        for i in nums:
            presum += i
            rem = presum % k
            if rem in d:
                ans += d[rem]
            if rem in d:
                d[rem] += 1
            else:
                d[rem] = 1
        return ans