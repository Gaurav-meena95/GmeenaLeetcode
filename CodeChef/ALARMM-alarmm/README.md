# [Welcome to the CodeChef AI Tutor](https://www.codechef.com/problems/ALARMM?tab=statement)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Learn problem solving techniques required to solve this problemTake our problem solving courses to understand how to attempt problems like these.Start LearningAlarmmm

*After escaping the abandoned arcade, Nikhil follows a narrow passage beneath the building and discovers an abandoned orbital station hidden underground. At its entrance lies a sealed security corridor, still guarded by an ancient system.*

The corridor contains NNN rooms arranged in a straight line. Some rooms still contain hostile sentry drones, and Nikhil must restore the station's security system before he can reach the control deck.

A binary string SSS describes the corridor: Si=1S_i=1Si​=1 means that the iii-th room is dangerous, while Si=0S_i=0Si​=0 means that it is safe.

Nikhil can install alarms in some of the rooms.

An alarm installed at room ppp (1≤p≤N1 \le p \le N1≤p≤N) protects all the rooms from max⁡(1,p−K)\max(1, p-K)max(1,p−K) through to ppp, inclusive of both ends.

An alarm protects the room where it is installed and rooms to its left; it does not protect any room to its right.

Determine the **minimum** number of alarms needed to protect every dangerous room.

Input Format

- The first line of input contains a single integer TTT, the number of test cases.

Each test case consists of two lines of input.

- The first line of each test case contains two integers NNN and KKK.

- The second line contains a binary string SSS of length NNN.

Output Format

For each test case, print one integer: the minimum number of alarms required to protect every dangerous room.

Constraints

- 1≤T≤1001 \le T \le 1001≤T≤100

- 1≤N≤1001 \le N \le 1001≤N≤100

- 0≤K≤N0 \le K \le N0≤K≤N

- SSS consists only of the characters `0` and `1`.

Sample 1:
InputOutput
```
4
5 2
00100
6 1
101010
8 0
01101001
7 3
1000011
```

```
1
3
4
2
```

Explanation:

**Test case 111:** Room 333 is the only dangerous room. An alarm installed in room 333 protects it.

**Test case 222:** Alarms installed in rooms 111, 333 and 555 protect all the dangerous rooms. It can be verified that fewer than 333 alarms are not enough.

**Test case 333:** Alarms installed in rooms 222, 333, 555 and 888 protect all the dangerous rooms. It can be verified that fewer than 444 alarms are not enough.

**Test case 444:** Alarms installed in rooms 444 and 777 protect rooms 111 to 444 and rooms 444 to 777 respectively, which covers all the dangerous rooms.
Did you like the problem statement?32 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)nikhil_010309Tester(s)raysh07Editorialist(s)iceknight1093
