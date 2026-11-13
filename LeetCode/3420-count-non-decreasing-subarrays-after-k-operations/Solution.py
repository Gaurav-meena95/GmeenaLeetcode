class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        cost = 0
        dq = collections.deque()
        n = len(nums)
        j = n - 1
        for i in range(n - 1, -1, -1):
            num = nums[i]
            count = 1
            while dq and dq[-1][0] < num:
                nextNum, nextCount = dq.pop()
                count += nextCount
                cost += (num - nextNum) * nextCount
            dq.append((num, count))
            while cost > k:
                rightnum, rightCount = dq.popleft()
                cost -= rightnum - nums[j]
                j -= 1
                if rightCount > 1:
                    dq.appendleft((rightnum, rightCount - 1))
            ans += j - i + 1
        return ans