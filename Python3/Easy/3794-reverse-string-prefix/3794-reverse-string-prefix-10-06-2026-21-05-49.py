class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        arr = list(s)
        r = k - 1
        l = 0
        while l < r:
            arr[r],arr[l] = arr[l],arr[r]
            l += 1
            r -= 1
        return ''.join(arr)


        