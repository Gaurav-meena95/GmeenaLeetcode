# [Scored](https://www.codechef.com/DSAMONDAY028/problems/BMC15A)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Practice problem - Apples and oranges

Rushitote went to a programming contest to distribute apples and oranges to the contestants.

He has NNN apples and MMM oranges, which need to be divided **equally** amongst the contestants. Find the maximum possible number of contestants such that:

- Every contestant gets an equal number of apples; and

- Every contestant gets an equal number of oranges.

Note that every fruit with Rushitote *must* be distributed, there cannot be any left over.

For example, 222 apples and 444 oranges can be distributed equally to two contestants, where each one receives 111 apple and 222 oranges.

However, 222 apples and 555 oranges can only be distributed equally to one contestant.

Input Format

- The first line of input will contain a single integer TTT, denoting the number of test cases.

- The first and only line of each test case contains two space-separated integers NNN and MMM — the number of apples and oranges, respectively.

Output Format

For each test case, output on a new line the answer: the maximum number of contestants such that everyone receives an equal number of apples and an equal number of oranges.

Constraints

- 1≤T≤10001 \leq T \leq 10001≤T≤1000

- 1≤N,M≤1091 \leq N , M \leq 10^91≤N,M≤109

Sample 1:
InputOutput
```
3
1 5
2 4
4 6
```

```
1
2
2
```

Explanation:

**Test case 111:** There's only one apple, so distributing to more than one person is impossible.

**Test case 222:** As explained in the statement, 222 people can each receive 111 apple and 222 oranges.

**Test case 333:** 222 people can each receive 222 apples and 333 oranges. It's not possible to distribute equally to more than two people.
Accepted360Submissions432Accuracy85.65Did you like the problem statement?6 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)admin
