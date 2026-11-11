# [Scored](https://www.codechef.com/START264D/problems/ROT4)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Rotational 4

You have a string SSS of length NNN, containing digits 000 to 999.

Out of the NNN cyclic shifts of SSS, find the number of them divisible by 444 when represented as a decimal number.

For example, for S=1080S = 1080S=1080, the cyclic shifts are 108010801080, 080108010801, 801080108010 and 010801080108, and out of these 108010801080, and 010801080108 are divisible by 444.

The NNN cyclic shifts of SSS can be described as: choose an integer iii (0≤i<N0 \le i < N0≤i<N) and then move the first character of the string SSS to the back iii times.

We distinguish 222 cyclic shifts by the integer iii chosen, even if the 222 strings end up the same.

Input Format

- The first line of input will contain a single integer TTT, denoting the number of test cases.

Each test case consists of multiple lines of input.

- The first line contains a single integer NNN.

- The second line contains a string SSS.

Output Format

For each test case, output on a new line the number of cyclic shifts divisible by 444.

Constraints

- 1≤T≤1041 \le T \le 10^41≤T≤104

- 2≤N≤2⋅1052 \le N \le 2 \cdot 10^52≤N≤2⋅105

- ∣S∣=N|S| = N∣S∣=N

- Si∈{0,1,…,9}S_i \in \{0, 1, \ldots, 9\}Si​∈{0,1,…,9}

- S1≠0S_1 \ne 0S1​=0

- The sum of NNN over all test cases does not exceed 2⋅1052 \cdot 10^52⋅105

Sample 1:
InputOutput
```
5
4
1080
3
444
3
222
4
4804
5
10001
```

```
2
3
0
4
2
```

Explanation:

**Test Case 1:** Described in the problem statement.

**Test Case 2:** All the cyclic shifts are 444444444, which is divisible by 444. We should output 333, since we still count them differently.
Accepted2605Submissions3786Accuracy76.31Did you like the problem statement?4 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)raysh07_admTester(s)iceknight1093Editorialist(s)iceknight1093
