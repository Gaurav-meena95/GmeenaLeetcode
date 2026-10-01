class Solution:
    def isValid(self, s: str) -> bool:
        test = '{[('
        stack =[]
        for i in s:
            if i in test:
                stack.append(i)
            else:
                if not stack :
                    return False
                top = stack.pop()
                if i == ")" and top !='(':
                    return False
                if i == "]" and top !='[':
                    return False
                if i == "}" and top !='{':
                    return False
        return len(stack) == 0



        
        