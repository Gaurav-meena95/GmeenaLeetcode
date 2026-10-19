# [Scored](https://www.codechef.com/DSAMONDAY025/problems/UNIQUE2)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Unique Elements 2

You are given an array AAA containing NNN integers. The array may contain duplicate elements.

Your task is to print all distinct elements of the array in the order of their first occurrence. Each element should appear exactly once in the output.

Input Format

- The first line contains an integer NNN, representing the size of the array.

- The second line contains NNN space-separated integers A1,A2,…,ANA_1, A_2, \ldots, A_NA1​,A2​,…,AN​, representing the array elements.

Output Format

Print all distinct elements separated by a single space, preserving their order of first occurrence.

Constraints

- 1≤N≤1051 \leq N \leq 10^51≤N≤105

- 1≤Ai≤1051 \leq A_i \leq 10^51≤Ai​≤105

Sample 1:
InputOutput
```
7
5 5 8 8 3 5 3
```

```
5 8 3
```

Explanation:

The elements 555, 888, and 333 appear for the first time in that order. Repeated occurrences are excluded from the output.

Sample 2:
InputOutput
```
9
12 7 12 4 7 15 4 9 15
```

```
12 7 4 15 9
```

Explanation:

The distinct elements are 121212, 777, 444, 151515, and 999, in the order of their first occurrence. All subsequent occurrences of these elements are ignored.
Accepted2682Submissions4694Accuracy62.08Did you like the problem statement?4 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 Bytes
