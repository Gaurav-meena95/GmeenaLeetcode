class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        Ama, Ada = map(int, arriveAlice.split("-"))
        Aml, Adl = map(int, leaveAlice.split("-"))
        bma, bda = map(int, arriveBob.split("-"))
        bml, bdl = map(int, leaveBob.split("-"))
        dayAa = sum(month[:Ama-1]) + Ada
        dayAl = sum(month[:Aml-1]) + Adl
        dayBa = sum(month[:bma-1]) + bda
        dayBl = sum(month[:bml-1]) + bdl
        ans = min(dayAl,dayBl) - max(dayAa,dayBa) + 1       
        if ans < 0:
            return 0
        return ans