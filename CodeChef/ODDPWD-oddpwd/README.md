# [Scored](https://www.codechef.com/START262D/problems/ODDPWD)

![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-orange)

## Problem Description
Odd Password

Hyder and Nikhil are stuck in an abandoned city and want to escape as soon as possible. The only way out is through the subway, but to start it, they must enter the correct password.

On their way, they picked up a mysterious string of exactly five characters. They suspect it holds the key to unlocking the subway, but they must figure out how to extract the password from it.

They also received a hint on how to obtain the password from the string, which says:

- The password consists of the 111-st, 333-rd and 555-th characters of the string, in that order.

Help them find the password and escape this chaos!

Input Format

- The input consists of a single line containing a string SSS of length 555.

Output Format

Print the password required to start the subway.

Constraints

- SSS has length 555.

- SSS contains only uppercase English letters

Sample 1:
InputOutput
```
ORDER
```

```
ODR
```

Explanation:

Looking at `ORDER`, the first character is `O`, the third is `D`, and the fifth is `R`. So, the password is `ODR`.

Sample 2:
InputOutput
```
CHAOS
```

```
CAS
```

Explanation:

Looking at `CHAOS`, the first character is `C`, the third is `A`, and the fifth is `S`. So, the password is `CAS`.

Sample 3:
InputOutput
```
WTETC
```

```
WEC
```

Explanation:

The password is `WEC`.
Accepted352Submissions399Accuracy88.72Did you like the problem statement?1 user found this helpfulMore InfoTime limit1 secsMemory limit1.5 GBSource Limit50000 BytesContributorsAuthor(s)hyder1102Tester(s)raysh07Editorialist(s)iceknight1093
