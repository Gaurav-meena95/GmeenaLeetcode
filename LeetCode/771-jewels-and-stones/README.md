# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Performance
- **Runtime**: 0 ms
- **Memory**: 19.2 MB

## Tags
`Hash Table` `String`

## Problem Description
You&#39;re given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

Example 1:

```
**Input:** jewels = "aA", stones = "aAAbbbb"
**Output:** 3
```

Example 2:

```
**Input:** jewels = "z", stones = "ZZ"
**Output:** 0
```

**Constraints:**

	- `1 <= jewels.length, stones.length <= 50`

	- `jewels` and `stones` consist of only English letters.

	- All the characters of `jewels` are **unique**.
