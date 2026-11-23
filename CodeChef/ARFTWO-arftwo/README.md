# [Scored](https://www.codechef.com/DSAMONDAY030/problems/ARFTWO)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
A Ride for Two

Chef and his two friends want to take a boat ride. They have AAA, BBB, and CCC rupees, respectively.

The boat can carry only two people, and a ride costs XXX rupees in total. The two people taking the ride must pay using their own money; the person staying behind cannot contribute.

Determine whether any two of them can afford the ride.

Input Format

- The first line contains an integer TTT, the number of test cases.

- Each test case contains four space-separated integers AAA, BBB, CCC, and XXX — the amounts of money the three friends have and the total cost of the ride.

Output Format

For each test case, print `YES` if any two friends can afford the ride, or `NO` otherwise, on a separate line.

You may print the answer in any combination of uppercase and lowercase letters.

Constraints

- 1≤T≤10001 \leq T \leq 10001≤T≤1000

- 1≤A,B,C,X≤1001 \leq A, B, C, X \leq 1001≤A,B,C,X≤100

Sample 1:
InputOutput
```
4
2 3 4 8
6 2 3 9
3 7 5 10
4 4 4 9
```

```
NO
YES
YES
NO
```

Explanation:

- **Test case 1:** No pair has more than 3+4=73+4=73+4=7 rupees, so they cannot afford the ride costing 888 rupees.

- **Test case 2:** Chef and the friend with 333 rupees can combine their money to pay exactly 999 rupees.

- **Test case 3:** The friends with 777 and 555 rupees have 121212 rupees together, enough for the ride costing 101010 rupees.

- **Test case 4:** Every pair has 888 rupees together, which is less than the cost of 999 rupees.

Accepted2078Submissions2748Accuracy81.08Did you like the problem statement?1 user found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 Bytes
