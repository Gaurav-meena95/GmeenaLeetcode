class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums) 
        def fn(mid,base):
            d = {}
            hash = 0
            p = (base ** (mid - 1)) % mod
            i = 0
            j = 0
            while j < n:
                hash = ((hash * base) + nums[j])% mod
                if j - i + 1 < mid:
                    j += 1
                else:
                    if hash in d:
                        d[hash] += 1
                    else:
                        d[hash] = 1
                    hash = (hash - (nums[i] * p)) % mod
                    i += 1
                    j += 1
            for k in d:
                if d[k] == 1:
                    return True
            return False
    
        base = max(nums) + 1
        ans = 0
        def binary(nums):
            nonlocal ans
            i = 1
            j = n 
            while i <= j:
                mid = (i + j) // 2
                if fn(mid,base):
                    ans = mid
                    j = mid - 1
                else:
                    i = mid + 1
        binary(nums)
        return ans