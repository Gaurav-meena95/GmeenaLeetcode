# [Scored](https://www.codechef.com/DSAMONDAY030/problems/BILBRA)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Books in Library

Chef has NNN books arranged in a row, where the iii-th book contains BiB_iBi​ pages. He wants to distribute all the books among AAA students so that each student receives a non-empty contiguous group of books. Every book must be assigned to exactly one student.

Find the **minimum** possible value of the **maximum** total number of pages assigned to any student.

Input Format

- The first line contains an integer TTT, the number of test cases.

For each test case:

- The first line contains two space-separated integers NNN and AAA: the number of books and the number of students.

- The second line contains NNN space-separated integers B1,B2,…,BNB_1, B_2, \ldots, B_NB1​,B2​,…,BN​: the number of pages in each book.

Output Format

For each test case, print the minimum possible maximum total number of pages assigned to a student, on a separate line.

Constraints

- 1≤T≤1001 \leq T \leq 1001≤T≤100

- 1≤N≤1051 \leq N \leq 10^51≤N≤105

- 1≤A≤N1 \leq A \leq N1≤A≤N

- 1≤Bi≤1051 \leq B_i \leq 10^51≤Bi​≤105

- The sum of NNN over all test cases won't exceed 2⋅1052 \cdot 10^52⋅105.

Sample 1:
InputOutput
```
2
5 2
4 8 2 6 10
5 5
10 5 10 12 18
```

```
16
18
```

Explanation:

**Test case 111**: First student will be allocated books [4,8,2][4, 8, 2][4,8,2], other student will be allocated books [6,10][6, 10][6,10]. So sum of pages will be 141414, 161616 and maximum of them will be 161616.

**Test case 222**: Each student will be allocated one book and maximum of them will be 181818.
Accepted661Submissions1195Accuracy59.25Did you like the problem statement?4 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 Bytes
