class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        nozero = 1
        zerocount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zerocount += 1
            product *= nums[i]

            if nums[i] != 0:
                nozero *= nums[i]
            
        ans = []
        if zerocount > 1:
            return [0] * len(nums)
        for i in nums:
            if zerocount ==1 and i == 0:
                ans.append(nozero)
            else:
                ans.append(product//i)
        return ans