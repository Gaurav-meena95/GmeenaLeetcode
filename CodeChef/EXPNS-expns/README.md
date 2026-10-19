# [Scored](https://www.codechef.com/DSAMONDAY025/problems/EXPNS)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Budget Feasibility

You are given two integers XXX and YYY, where XXX represents the available budget and YYY represents the amount required per day.

The budget must cover expenses for exactly 303030 days.

Determine whether the available budget is sufficient to cover the total expenses for all 303030 days.

Input Format

- The first line contains an integer TTT, representing the number of test cases.

- Each test case contains two space-separated integers XXX and YYY, representing the available budget and the daily expense.

Output Format

For each test case, print `YES` if the budget is sufficient to cover the expenses for 303030 days. Otherwise, print `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

Constraints

- 1≤T≤1001 \leq T \leq 1001≤T≤100

- 1≤X,Y≤1051 \leq X, Y \leq 10^51≤X,Y≤105

Sample 1:
InputOutput
```
4
900 30
500 20
1200 35
100 4
```

```
YES
NO
YES
NO
```

Explanation:

- **Test Case 1:** The total expense is 30×30=90030 \times 30 = 90030×30=900. Since X=900X = 900X=900, the budget is sufficient.

- **Test Case 2:** The total expense is 30×20=60030 \times 20 = 60030×20=600. Since X=500X = 500X=500, the budget is insufficient.

- **Test Case 3:** The total expense is 30×35=105030 \times 35 = 105030×35=1050. Since X=1200X = 1200X=1200, the budget is sufficient.

- **Test Case 4:** The total expense is 30×4=12030 \times 4 = 12030×4=120. Since X=100X = 100X=100, the budget is insufficient.

Accepted3390Submissions4700Accuracy82.28Did you like the problem statement?7 users found this helpfulMore InfoTime limit0.5 secsMemory limit1.5 GBSource Limit50000 Bytes
