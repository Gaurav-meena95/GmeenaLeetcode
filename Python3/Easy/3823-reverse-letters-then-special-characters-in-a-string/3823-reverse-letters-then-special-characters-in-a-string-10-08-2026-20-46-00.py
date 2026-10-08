class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s)
        ch = "!@#$%^&*()"
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in ch and s[j] not in ch:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
            elif s[i] in ch:
                i += 1
            else:
                j -= 1
        a,b = 0 , len(s)-1
        while a < b:
            if s[a] in ch and s[b]  in ch:
                s[a],s[b] = s[b],s[a]
                a += 1
                b -= 1
            elif s[a]  not in ch:
                a += 1
            else:
                b -= 1
        return ''.join(s)





        