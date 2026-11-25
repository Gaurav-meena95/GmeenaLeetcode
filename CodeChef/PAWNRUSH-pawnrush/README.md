# [Scored](https://www.codechef.com/START266D/problems/PAWNRUSH)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Pawn Rush

Chef is practising chess endgames. A white pawn stands on row RRR of an otherwise empty 8×88 \times 88×8 chessboard. The rows are numbered 111 to 888 from White's side, so the pawn moves towards row 888.

In one move, the pawn moves forward by one row. However, a pawn standing on row 222 (its starting row) may instead move forward by **two** rows in that move.

Find the minimum number of moves the pawn needs to reach row 888.

Input Format

- The first and only line of input contains a single integer RRR — the row the pawn stands on.

Output Format

Output a single integer — the minimum number of moves the pawn needs to reach row 888.

Constraints

- 2≤R≤72 \leq R \leq 72≤R≤7

Sample 1:
InputOutput
```
7
```

```
1
```

Explanation:

The pawn moves from row 777 to row 888 in one move.

Sample 2:
InputOutput
```
2
```

```
5
```

Explanation:

The pawn first moves two rows, from row 222 to row 444, and then one row at a time to rows 555, 666, 777 and 888. That is 555 moves in total.
Accepted1978Submissions2605Accuracy79.08Did you like the problem statement?3 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)raysh07_admTester(s)iceknight1093Editorialist(s)iceknight1093
