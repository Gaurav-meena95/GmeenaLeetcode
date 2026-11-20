class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = date.split('-')
        ans = str(bin(int(arr[0]))[2:])
        for i in range(1,len(arr)):
            ans += '-' + str(bin(int(arr[i]))[2:])
        return ans