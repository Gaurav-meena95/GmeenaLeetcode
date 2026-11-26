# [3760. Maximum Substrings With Distinct Start](https://leetcode.com/problems/maximum-substrings-with-distinct-start/)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Performance
- **Runtime**: 60 ms
- **Memory**: 19.9 MB

## Tags
`Hash Table` `String`

## Problem Description
You are given a string `s` consisting of lowercase English letters.

Return an integer denoting the **maximum** number of substrings you can split `s` into such that each **substring** starts with a **distinct** character (i.e., no two substrings start with the same character).

Example 1:

**Input:** s = "abab"

**Output:** 2

**Explanation:**

	- Split `"abab"` into `"a"` and `"bab"`.

	- Each substring starts with a distinct character i.e `&#39;a&#39;` and `&#39;b&#39;`. Thus, the answer is 2.

Example 2:

**Input:** s = "abcd"

**Output:** 4

**Explanation:**

	- Split `"abcd"` into `"a"`, `"b"`, `"c"`, and `"d"`.

	- Each substring starts with a distinct character. Thus, the answer is 4.

Example 3:

**Input:** s = "aaaa"

**Output:** 1

**Explanation:**

	- All characters in `"aaaa"` are `&#39;a&#39;`.

	- Only one substring can start with `&#39;a&#39;`. Thus, the answer is 1.

**Constraints:**

	- `1 <= s.length <= 105`

	- `s` consists of lowercase English letters.
