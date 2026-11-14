class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')
        for i in range(1,n):
            nums[i] += nums[i-1]
        nums.insert(0,0)
        for  left in range(0,n-l+1):
            for right in range(left+l,min(left+r,n)+1):
                add = nums[right]- nums[left]
                if add > 0:
                    ans  = min(ans,add)
        if ans == float('inf'):
            return -1
        return ans