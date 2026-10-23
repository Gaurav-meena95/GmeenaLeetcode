class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = None
        for i ,ele in enumerate(nums):
            if i != ele:
                if ans is None:
                    ans = ele
                else:
                    ans &= ele
        return 0 if ans is None else ans