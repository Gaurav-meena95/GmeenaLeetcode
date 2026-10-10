
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        low, high = 0, max(diff)

        while low < high:
            mid = (low + high) // 2

            ops = sum(max(0, d - mid) for d in diff)

            if ops <= k:
                high = mid
            else:
                low = mid + 1

        level = low
        ops = sum(max(0, d - level) for d in diff)
        ans = sum(min(d, level) ** 2 for d in diff)

        remaining = k - ops

        count = sum(d >= level for d in diff)
        ans -= min(remaining, count) * (2 * level - 1)

        return ans
