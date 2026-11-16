class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            curr = ''
            for i in range(0,len(s),k):
                num = sum(list(map(int,s[i:i +k])))
                curr += str(num)
            s = curr
        return s