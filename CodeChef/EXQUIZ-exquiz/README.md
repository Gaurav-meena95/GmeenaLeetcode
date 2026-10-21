# [Scored](https://www.codechef.com/START261D/problems/EXQUIZ)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Exun Quiz

The prelims of the Exun quiz have NNN questions. A correct answer earns 444 points, a wrong answer costs 111 point, and a skipped question gives 000 points.

After the prelims, a team walks up to the quizmaster with a final score of SSS. The quizmaster is curious: what is the smallest number of questions the team could have attempted (answered correctly or wrongly) to finish with exactly SSS points? If no way of answering the NNN questions gives exactly SSS points, the scoresheet must contain an error.

Input Format

- The first line of input contains a single integer TTT, denoting the number of test cases.

- Each test case consists of a single line containing two space-separated integers NNN and SSS.

Output Format

For each test case, output on a new line the minimum number of attempted questions, or −1-1−1 if a score of exactly SSS is impossible.

Constraints

- 1≤T≤100001 \leq T \leq 100001≤T≤10000

- 1≤N≤501 \leq N \leq 501≤N≤50

- 0≤S<200 0 \leq S \lt 2000≤S<200

Sample 1:
InputOutput
```
6
10 7
10 9
10 40
7 0
1 3
1 5
```

```
3
6
10
0
-1
-1
```

Explanation:

Test case 111: 222 correct answers and 111 wrong answer give 8−1=78 - 1 = 78−1=7 points with 333 attempts.

Test case 444: Since the final score is 000, all questions can be skipped.
Accepted2947Submissions3524Accuracy86.41Did you like the problem statement?5 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)am_aadvikTester(s)iceknight1093Editorialist(s)iceknight1093
