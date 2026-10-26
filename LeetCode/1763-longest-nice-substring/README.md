# [1763. Longest Nice Substring](https://leetcode.com/problems/longest-nice-substring/)

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen)

## Performance
- **Runtime**: N/A
- **Memory**: N/A

## Tags
`Hash Table` `String` `Divide and Conquer` `Bit Manipulation` `Sliding Window`

## Problem Description
A string `s` is **nice** if, for every letter of the alphabet that `s` contains, it appears **both** in uppercase and lowercase. For example, `"abABB"` is nice because `&#39;A&#39;` and `&#39;a&#39;` appear, and `&#39;B&#39;` and `&#39;b&#39;` appear. However, `"abA"` is not because `&#39;b&#39;` appears, but `&#39;B&#39;` does not.

Given a string `s`, return *the longest **substring** of `s` that is **nice**. If there are multiple, return the substring of the **earliest** occurrence. If there are none, return an empty string*.

Example 1:

```
**Input:** s = "YazaAay"
**Output:** "aAa"
**Explanation: **"aAa" is a nice string because &#39;A/a&#39; is the only letter of the alphabet in s, and both &#39;A&#39; and &#39;a&#39; appear.
"aAa" is the longest nice substring.
```

Example 2:

```
**Input:** s = "Bb"
**Output:** "Bb"
**Explanation:** "Bb" is a nice string because both &#39;B&#39; and &#39;b&#39; appear. The whole string is a substring.
```

Example 3:

```
**Input:** s = "c"
**Output:** ""
**Explanation:** There are no nice substrings.
```

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of uppercase and lowercase English letters.
