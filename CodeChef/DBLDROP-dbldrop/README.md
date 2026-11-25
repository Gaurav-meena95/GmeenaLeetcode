# [Scored](https://www.codechef.com/START266D/problems/DBLDROP)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Double and Drop (Easy)

You are given an array AAA of NNN positive integers.

You may perform the following operation **at most once**:

- Choose an index iii (1≤i≤N1 \le i \le N1≤i≤N) and set Ai:=2⋅AiA_i := 2 \cdot A_iAi​:=2⋅Ai​.

After that, let f(A)f(A)f(A) be the maximum possible value of sum(A)−max⁡(A)\text{sum}(A) - \max(A)sum(A)−max(A), that is, the sum of all its elements except one copy of the largest one.

Given an array of NNN elements, find f(A)f(A)f(A).

Input Format

- The first line of input will contain a single integer TTT, denoting the number of test cases.

Each test case consists of two lines of input.

- The first line of each test case contains a single integer NNN — the length of the array.

- The second line contains NNN space-separated integers A1,A2,…,ANA_1, A_2, \ldots, A_NA1​,A2​,…,AN​.

Output Format

For each test case, output on a new line the maximum possible score f(A)f(A)f(A).

Constraints

- 1≤T≤10001 \leq T \leq 10001≤T≤1000

- 2≤N≤50002 \leq N \leq 50002≤N≤5000

- 1≤Ai≤1091 \leq A_i \leq 10^91≤Ai​≤109

- The sum of NNN over all test cases does not exceed 500050005000.

Sample 1:
InputOutput
```
4
3
1 2 3
2
5 5
3
1 6 10
5
7 3 9 2 9
```

```
4
5
11
24
```

Explanation:

**Test case 111:** Doubling A1A_1A1​ gives [2,2,3][2, 2, 3][2,2,3], with score 7−3=47 - 3 = 47−3=4. Doubling A2A_2A2​ gives [1,4,3][1, 4, 3][1,4,3], with score 8−4=48 - 4 = 48−4=4 as well. No choice does better.

**Test case 222:** Without the operation, the score is 10−5=510 - 5 = 510−5=5. Doubling either element gives score 15−10=515 - 10 = 515−10=5.

**Test case 333:** Doubling A2A_2A2​ gives [1,12,10][1, 12, 10][1,12,10]. The maximum changes, but the score is 23−12=1123 - 12 = 1123−12=11, which is optimal.
Accepted988Submissions1529Accuracy68.28Did you like the problem statement?2 users found this helpfulMore InfoTime limit2 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)raysh07_admTester(s)iceknight1093Editorialist(s)iceknight1093
