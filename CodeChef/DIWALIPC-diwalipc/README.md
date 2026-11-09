# [Scored](https://www.codechef.com/DSAMONDAY028/problems/DIWALIPC)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Diwali PC Build

Chef wants to build a PC for Diwali, which is KKK days away.

The components currently cost PPP rupees in total, including RAM. The RAM price increases by DDD rupees each day, while all other prices remain unchanged.

Chef has decided to buy the components on Diwali. Will his budget of BBB rupees be enough?

Input Format

- The first line contains an integer TTT, the number of test cases.

- Each test case contains four space-separated integers PPP, DDD, KKK, and BBB — the current total cost, the daily increase in RAM price, the number of days until Diwali, and Chef's budget, respectively.

Output Format

For each test case, print `YES` if Chef can afford all the components on Diwali, or `NO` otherwise, on a separate line.

You may print the answer in any combination of uppercase and lowercase letters.

Constraints

- 1≤T≤1001 \le T \le 1001≤T≤100

- 1≤P,B≤1051 \le P,B \le 10^51≤P,B≤105

- 1≤D≤5001 \le D \le 5001≤D≤500

- 0≤K≤300 \le K \le 300≤K≤30

Sample 1:
InputOutput
```
4
100 10 2 120
200 20 3 250
150 5 4 180
100 10 0 90
```

```
YES
NO
YES
NO
```

Explanation:

- **Test case 1:** After 222 days, the total cost is 100+10×2=120100 + 10 \times 2 = 120100+10×2=120 rupees. Chef's budget exactly covers the cost.

- **Test case 2:** After 333 days, the total cost is 200+20×3=260200 + 20 \times 3 = 260200+20×3=260 rupees, which exceeds his budget of 250250250 rupees.

- **Test case 3:** After 444 days, the total cost is 150+5×4=170150 + 5 \times 4 = 170150+5×4=170 rupees, which is within his budget of 180180180 rupees.

- **Test case 4:** Diwali is today, so the total cost remains 100100100 rupees. His budget of 909090 rupees is insufficient.

Accepted392Submissions440Accuracy91.59Did you like the problem statement?More InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 Bytes
