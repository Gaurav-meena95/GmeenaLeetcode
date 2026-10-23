# [3258. Count Substrings That Satisfy K-Constraint I](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Performance
- **Runtime**: N/A
- **Memory**: N/A

## Tags
`String` `Sliding Window`

## Problem Description
You are given a **binary** string `s` and an integer `k`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

	- The number of `0`&#39;s in the string is at most `k`.

	- The number of `1`&#39;s in the string is at most `k`.

Return an integer denoting the number of substrings of `s` that satisfy the **k-constraint**.

Example 1:

**Input:** s = "10101", k = 1

**Output:** 12

**Explanation:**

Every substring of `s` except the substrings `"1010"`, `"10101"`, and `"0101"` satisfies the k-constraint.

Example 2:

**Input:** s = "1010101", k = 2

**Output:** 25

**Explanation:**

Every substring of `s` except the substrings with a length greater than 5 satisfies the k-constraint.

Example 3:

**Input:** s = "11111", k = 1

**Output:** 15

**Explanation:**

All substrings of `s` satisfy the k-constraint.

**Constraints:**

	- `1 <= s.length <= 50 `

	- `1 <= k <= s.length`

	- `s[i]` is either `&#39;0&#39;` or `&#39;1&#39;`.
