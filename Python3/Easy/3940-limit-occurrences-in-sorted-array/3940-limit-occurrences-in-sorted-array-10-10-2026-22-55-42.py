class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1] :
                count = 0
            if count < k:
                count += 1
                ans.append(nums[i])

        return ans
                



        