# [Scored](https://www.codechef.com/START266D/problems/EXACTKMOVES)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Exactly K Moves

Chef is climbing a staircase with NNN steps. In one move, he climbs either 111 step or 222 steps.

Chef's fitness watch wants him to reach the top of the staircase (step NNN) in **exactly** KKK moves. He must not go past the top.

Determine whether this is possible.

Input Format

- The first line of input will contain a single integer TTT, denoting the number of test cases.

- The first and only line of each test case contains two space-separated integers NNN and KKK — the number of steps and the required number of moves.

Output Format

For each test case, output on a new line `YES` if Chef can reach the top in exactly KKK moves, and `NO` otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e., the strings `NO`, `no`, `nO`, and `No` will all be treated as equivalent.

Constraints

- 1≤T≤10001 \leq T \leq 10001≤T≤1000

- 1≤N,K≤10001 \leq N, K \leq 10001≤N,K≤1000

Sample 1:
InputOutput
```
4
5 3
5 2
3 4
4 2
```

```
YES
NO
NO
YES
```

Explanation:

**Test case 111:** Chef can climb 222, 222 and then 111 steps.

**Test case 222:** In 222 moves, Chef climbs at most 444 steps, so he cannot reach step 555.

**Test case 333:** In 444 moves, Chef climbs at least 444 steps, which is more than the 333 steps of the staircase.

**Test case 444:** Chef climbs 222 steps twice.
Accepted1961Submissions2692Accuracy79.27Did you like the problem statement?2 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)raysh07_admTester(s)iceknight1093Editorialist(s)iceknight1093
