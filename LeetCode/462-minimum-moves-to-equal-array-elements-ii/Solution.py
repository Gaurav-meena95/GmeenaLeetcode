class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        maxans = 0
        minans = 0 
        for i in nums:
            print(maxi ,i)
            maxans += maxi - i
            minans += i - mini 
        print(maxans,minans)
        return min(maxans,minans)