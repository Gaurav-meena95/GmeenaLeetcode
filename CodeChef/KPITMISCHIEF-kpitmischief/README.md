# [Scored](https://www.codechef.com/DSAMONDAY028/problems/KPITMISCHIEF)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Largest Mischievous Group

You are the principal of a school that has some mischievous students. The students stand in a
row, described by a string of length NNN: the character `m` is a mischievous student and `g` is a
good student.

A **mischievous group** is a maximal block of one or more consecutive `m` characters. Find the
largest mischievous group and print its starting and ending positions (both inclusive), with
positions numbered from 000. If several groups have the maximum length, report the one that
appears first.

Input Format

- The first line contains an integer NNN - the length of the string.

- The second line contains a string of length NNN consisting of the characters `m` and `g`.

Output Format

Print two space-separated integers: the starting and the ending index of the largest
mischievous group.

Constraints

- 1≤N≤1051 \leq N \leq 10^51≤N≤105

- The string contains only `m` and `g`, and at least one `m`.

Sample 1:
InputOutput
```
5
mgmmm
```

```
2 4
```

Explanation:

The groups are [0,0][0, 0][0,0] (length 111) and [2,4][2, 4][2,4] (length 333). The largest is [2,4][2, 4][2,4].

Sample 2:
InputOutput
```
8
mmgmmgmg
```

```
0 1
```

Explanation:

The groups [0,1][0, 1][0,1] and [3,4][3, 4][3,4] both have length 222; the first one is reported.

Sample 3:
InputOutput
```
4
gggm
```

```
3 3
```

Explanation:

The only group is the single student at index 333.
Accepted896Submissions1354Accuracy69.05Did you like the problem statement?2 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)abhay_1006
