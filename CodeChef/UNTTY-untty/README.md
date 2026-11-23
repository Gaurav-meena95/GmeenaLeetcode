# [Scored](https://www.codechef.com/DSAMONDAY030/problems/UNTTY)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Undo the Typos

Sara types on a keyboard that has only lowercase English letters (`a`–`z`) and the `#` key, which works like Backspace.

She starts with an empty text and processes the characters of a string SSS from left to right:

- A lowercase letter is appended to the end of the current text.

- A `#` removes the last character of the current text. If the text is already empty, `#` has no effect.

Find the **final text** after all characters of SSS have been processed.

Input Format

The only line contains the string SSS.

Output Format

Print the final text on a single line. If the final text is empty, do not print anything.

Constraints

- 1≤∣S∣≤1051 \le |S| \le 10^51≤∣S∣≤105

- SSS consists only of lowercase English letters and `#`.

Sample 1:
InputOutput
```
abc#d##
```

```
a
```

Explanation:

After typing `abc`, the first `#` removes `c`, leaving `ab`. Typing `d` produces `abd`. The remaining two `#` characters remove `d` and then `b`, leaving `a`.

Sample 2:
InputOutput
```
abc##de#
```

```
ad
```

Explanation:

After typing `abc`, the next two `#` characters remove `c` and then `b`, leaving `a`. Typing `de` produces `ade`. The final `#` removes `e`, leaving `ad`.

Sample 3:
InputOutput
```
#a##b#
```

```

```

Explanation:

The first `#` does nothing because the text is empty. Typing `a` gives `a`, and the next `#` removes it. The second `#` again does nothing on empty text. Typing `b` gives `b`, and the last `#` removes it, leaving the text empty.
Accepted1489Submissions2356Accuracy67.06Did you like the problem statement?2 users found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 Bytes
