class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        count = [0] * 30

        for x in nums:
            for b in range(30):
                if x >> b & 1:
                    count[b] += 1

        ans = 0
        for _ in range(k):
            x = 0
            for b in range(30):
                if count[b]:
                    x |= 1 << b
                    count[b] -= 1
            ans = (ans + x * x) % mod

        return ans
        