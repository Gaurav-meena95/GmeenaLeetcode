# [Scored](https://www.codechef.com/START266D/problems/ROYALTOUR)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Royal Tour

Chef has a king on a chessboard with NNN rows and MMM columns. The rows are numbered 111 to NNN from top to bottom, and the columns are numbered 111 to MMM from left to right. The king starts at cell (r,c)(r, c)(r,c).

In one move, the king can go to any cell adjacent to its current cell horizontally, vertically or diagonally (up to 888 cells), without leaving the board.

Find the minimum number of moves the king needs to visit all four corner cells (1,1)(1, 1)(1,1), (1,M)(1, M)(1,M), (N,1)(N, 1)(N,1) and (N,M)(N, M)(N,M).

The corners may be visited in any order, and the king may finish anywhere. A corner counts as visited if the king stands on it at any moment, including the start.

Input Format

- The first line of input will contain a single integer TTT, denoting the number of test cases.

Each test case consists of two lines of input.

- The first line of each test case contains two space-separated integers NNN and MMM — the number of rows and columns of the board.

- The second line contains two space-separated integers rrr and ccc — the starting cell of the king.

Output Format

For each test case, output on a new line the minimum number of moves the king needs to visit all four corners.

Constraints

- 1≤T≤1041 \leq T \leq 10^41≤T≤104

- 1≤N,M≤1091 \leq N, M \leq 10^91≤N,M≤109

- 1≤r≤N1 \leq r \leq N1≤r≤N

- 1≤c≤M1 \leq c \leq M1≤c≤M

Sample 1:
InputOutput
```
4
2 5
1 1
3 3
2 2
1 10
1 4
4 7
2 6
```

```
6
7
12
13
```

Explanation:

**Test case 111:** The king moves from (1,1)(1, 1)(1,1) to (2,1)(2, 1)(2,1), then along row 222 to (2,5)(2, 5)(2,5), and finally to (1,5)(1, 5)(1,5). This takes 1+4+1=61 + 4 + 1 = 61+4+1=6 moves.

**Test case 222:** The king first moves to (1,1)(1, 1)(1,1), and then visits (1,3)(1, 3)(1,3), (3,3)(3, 3)(3,3) and (3,1)(3, 1)(3,1) in this order, using 222 moves for each. This takes 1+2+2+2=71 + 2 + 2 + 2 = 71+2+2+2=7 moves.

**Test case 333:** The board has a single row, so the corners are just cells (1,1)(1, 1)(1,1) and (1,10)(1, 10)(1,10). The king walks 333 moves left to (1,1)(1, 1)(1,1) and then 999 moves right to (1,10)(1, 10)(1,10).
Accepted680Submissions1025Accuracy72.78Did you like the problem statement?More InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)raysh07_admTester(s)iceknight1093Editorialist(s)iceknight1093
