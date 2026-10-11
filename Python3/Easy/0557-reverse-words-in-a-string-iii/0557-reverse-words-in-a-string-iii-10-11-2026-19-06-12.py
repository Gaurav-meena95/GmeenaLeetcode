class Solution:
    def reverseWords(self, s: str) -> str:
        def fn(p):
            st = p[::-1]
            # st += ' '
            return st
        arr = []
        curr = ''
        for i in s:
            if i == ' ':
                arr.append(fn(curr))
                curr = ''
            else:
                curr += i
        arr.append(curr[::-1])
        return ' '.join(arr)
        