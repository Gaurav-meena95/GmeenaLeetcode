class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        def isvalid(s):
            c = 0
            for i in s:
                if c < 0:
                    return False
                if i  == '(':
                    c += 1
                else:
                    c -= 1
            return c == 0
        curr = []
        ans = []
        def fn(i,j,curr):
            if len(curr) == 2*n:
                s = ''.join(curr)
                print(s)
                if isvalid(s):
                    ans.append(s)
            if i < n:
                curr.append('(')
                fn(i + 1,j,curr)
                curr.pop()
            if j < n:
                curr.append(')')
                fn(i,j + 1,curr)
                curr.pop()
        fn(0,0,curr)
        return ans


        