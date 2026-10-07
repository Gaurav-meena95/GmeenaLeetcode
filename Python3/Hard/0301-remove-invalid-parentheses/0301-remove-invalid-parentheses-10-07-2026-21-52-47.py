class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        set_arr = set()
        curr = []
        maxlen = [0]
        def fn(i,c):
            if c < 0:
                return
            if i == len(s):
                if c == 0:
                    set_arr.add("".join(curr))
                    if len(curr) > maxlen[0]:
                        maxlen[0] = len(curr)
                return
            if s[i] != '(' and s[i] != ')':
                curr.append(s[i])
                fn(i + 1,c)
                curr.pop()
                return
            curr.append(s[i])
            fn(i + 1, c + (1 if s[i] == '(' else -1))
            curr.pop()
            fn(i + 1,c)

        fn(0,0)
        ans = []
        for i in set_arr:
            if len(i) == maxlen[0]:
                ans.append(i)
        return ans


        