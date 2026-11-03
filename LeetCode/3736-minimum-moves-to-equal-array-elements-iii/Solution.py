class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mini  = max(nums)
        ans = 0
        for i in nums:
            ans += mini - i
        return ans