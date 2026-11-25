class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base(num,base):
            if num == 0:
                return '0'
            digit = ''
            while num>0:
                rem = num % base
                digit = str(rem) + digit
                num = num // base
            return digit
        def isplandrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        for i in range(2,n-1):
            num = to_base(n,i)
            if not isplandrome(num):
                return False
        return True