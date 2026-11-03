# [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Performance
- **Runtime**: 55 ms
- **Memory**: 39 MB

## Tags
`Array` `Hash Table` `Sliding Window`

## Problem Description
Given an integer array `nums` and an integer `k`, return `true` *if there are two **distinct indices** *`i`* and *`j`* in the array such that *`nums[i] == nums[j]`* and *`abs(i - j) <= k`.

Example 1:

```
**Input:** nums = [1,2,3,1], k = 3
**Output:** true
```

Example 2:

```
**Input:** nums = [1,0,1,1], k = 1
**Output:** true
```

Example 3:

```
**Input:** nums = [1,2,3,1,2,3], k = 2
**Output:** false
```

**Constraints:**

	- `1 <= nums.length <= 105`

	- `-109 <= nums[i] <= 109`

	- `0 <= k <= 105`
