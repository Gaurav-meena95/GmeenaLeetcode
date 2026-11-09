class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sumn = 0
        for i in nums:
            sumn += i
        return sumn%k