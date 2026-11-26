class Solution:
    def canAliceWin(self, n: int) -> bool:
        canpick = 10
        a = 0
        b = 0
        while n >= canpick:
            if n >= canpick and canpick % 2 == 0:
                a += 1
                n -= canpick
                canpick -= 1
            elif n >= canpick and canpick % 2 == 1:
                b += 1
                n -= canpick
                canpick -= 1
        return not a == b