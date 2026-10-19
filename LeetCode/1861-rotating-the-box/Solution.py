class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        rotatedBox = [['.'] * m for _ in range(n)] 
        for i in range(n):
            for j in range(m):
                rotatedBox[i][j] = boxGrid[j][i]
        for row in rotatedBox:
            row.reverse()
        for j in range(m):
            for i in range(n-1,-1,-1):
                if rotatedBox[i][j] == '.' :
                    stonerow = -1
                    for k in range(i-1,-1,-1):
                        if rotatedBox[k][j] == '*':
                            break
                        elif rotatedBox[k][j] == '#':
                            stonerow = k
                            break
                    if stonerow != -1:
                        rotatedBox[i][j] = '#'
                        rotatedBox[stonerow][j] = '.'
        return rotatedBox

        return rotatedBox




        