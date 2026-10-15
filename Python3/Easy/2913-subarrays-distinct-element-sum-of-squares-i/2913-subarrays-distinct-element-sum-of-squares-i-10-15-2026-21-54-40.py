class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        arr = set()
        ans = 0
        for i in range(len(nums)):
            arr = set()
            for j in nums[i:]:
                arr.add(j)
                ans += len(arr)**2
        return ans




        