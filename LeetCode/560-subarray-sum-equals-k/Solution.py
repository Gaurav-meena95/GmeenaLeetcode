class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        d = {0:1}
        ans = 0
        for i in nums:
            curr += i
            if curr - k in d:
                ans += d[curr - k]
            if curr in d:
                d[curr] += 1
            else:
                d[curr] = 1
        return ans