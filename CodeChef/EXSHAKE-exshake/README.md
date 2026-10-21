# [Scored](https://www.codechef.com/START261D/problems/EXSHAKE)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Exun Handshake

NNN groups of participants are trying to reach the annual Exun symposium. Group iii has AiA_iAi​ people.

By tradition, everyone at the symposium shakes hands with everyone else exactly once as a sign of sportsmanship, whether they are from the same group or not. So if PPP people attend in total, there are P(P−1)2\frac{P(P-1)}{2}2P(P−1)​ handshakes.

The ceremony takes a long time, and the organisers only have time for MMM handshakes. They will invite some of the groups (a group comes in full or not at all) so that the total number of handshakes is at most MMM.

Find the maximum number of groups that can be invited.

Inviting no groups at all is allowed, and gives 000 handshakes.

Input Format

- The first line of input contains a single integer TTT, denoting the number of test cases.

Each test case consists of two lines of input.

- The first line of each test case contains two space-separated integers NNN and MMM.

- The second line contains NNN space-separated integers A1,A2,…,ANA_1, A_2, \ldots, A_NA1​,A2​,…,AN​.

Output Format

For each test case, output on a new line the maximum number of groups that can be invited.

Constraints

- 1≤T≤1001 \leq T \leq 1001≤T≤100

- 1≤N≤1001 \leq N \leq 1001≤N≤100

- 0≤M≤1080 \leq M \leq 10^80≤M≤108

- 1≤Ai≤1001 \leq A_i \leq 1001≤Ai​≤100

Sample 1:
InputOutput
```
4
4 10
3 1 4 2
3 0
2 5 3
5 45
2 2 2 2 2
3 0
4 1 1
```

```
2
0
5
1
```

Explanation:

Test case 111: Inviting the groups with 111 and 222 people gives 333 people and 3⋅22=3\frac{3 \cdot 2}{2} = 323⋅2​=3 handshakes. Any 333 groups bring at least 1+2+3=61 + 2 + 3 = 61+2+3=6 people, which means at least 15>1015 > 1015>10 handshakes.
Accepted1883Submissions2192Accuracy87.77Did you like the problem statement?7 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)am_aadvikTester(s)iceknight1093Editorialist(s)iceknight1093
