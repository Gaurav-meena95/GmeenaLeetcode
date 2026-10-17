class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        for i, val in enumerate(nums):
            d_sum = sum(int(d) for d in str(val))
            arr.append((d_sum, val, i))
        arr.sort()
        visited = [False] * n
        ans = 0
        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue
                
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
                
            if cycle_size > 0:
                ans += (cycle_size - 1)
                
        return ans


