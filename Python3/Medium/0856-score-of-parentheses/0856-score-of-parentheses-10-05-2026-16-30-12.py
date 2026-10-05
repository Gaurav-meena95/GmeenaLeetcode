class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = []
        score = 0
        for i in range(len(s)):
            if s[i] == '(':
                ans.append(score)
                score = 0
            else:
                if s[i-1] == '(':
                    score  = ans.pop() + 1
                else:
                    score = ans.pop() + (2 * score)
        return score
