import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:

        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sub = nums[i:j]
                gcd = math.gcd(*sub)
                lcm = math.lcm(*sub)
                prod = math.prod(sub)
                if prod == lcm * gcd:
                    ans = max(len(sub),ans)
        return ans