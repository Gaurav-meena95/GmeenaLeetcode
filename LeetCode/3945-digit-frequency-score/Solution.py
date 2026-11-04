class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d = {}
        while n > 0:
            digi = n % 10
            if digi in d:
                d[digi] += 1
            else:
                d[digi] = 1
            n = n//10
        ans = 0
        for i in d:
            ans += i * d[i]
        return ans