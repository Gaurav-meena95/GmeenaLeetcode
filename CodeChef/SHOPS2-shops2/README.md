# [Scored](https://www.codechef.com/START264D/problems/SHOPS2)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Shopping 2

Chef wants to buy NNN items. There are 222 shops selling each of these items.

The iii-th item costs AiA_iAi​ rupees at shop 111, and BiB_iBi​ at shop 222.

Chef needs to spend DDD rupees to go to one of the shops, so if he wants to go to both, he will need to spend 2⋅D2 \cdot D2⋅D rupees.

Find the minimum cost for Chef to buy all of the items 111 through NNN.

Input Format

- The first line of input will contain a single integer TTT, denoting the number of test cases.

Each test case consists of multiple lines of input.

- The first line contains 222 integers NNN and DDD.

- The second line contains NNN integers - A1,A2,…,ANA_1, A_2, \ldots, A_NA1​,A2​,…,AN​.

- The third line contains NNN integers - B1,B2,…,BNB_1, B_2, \ldots, B_NB1​,B2​,…,BN​.

Output Format

For each test case, output on a new line the minimum cost Chef needs to pay.

Constraints

- 1≤T≤1001 \le T \le 1001≤T≤100

- 1≤N≤1001 \le N \le 1001≤N≤100

- 1≤Ai,Bi,D≤1001 \le A_i, B_i, D \le 1001≤Ai​,Bi​,D≤100

Sample 1:
InputOutput
```
3
3 100
1 2 3
3 1 1
3 5
1 10 10
10 1 12
4 1
1 2 3 4
4 3 2 1
```

```
105
22
8
```

Explanation:

**Test Case 1:** Chef will go only to shop 222, and buy all items there. This will cost him D+B1+B2+B3=105D + B_1 + B_2 + B_3 = 105D+B1​+B2​+B3​=105.

If Chef went to both stores, the cost would be ≥200\ge 200≥200.
Accepted1817Submissions2172Accuracy87.89Did you like the problem statement?4 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)raysh07_admTester(s)iceknight1093Editorialist(s)iceknight1093
