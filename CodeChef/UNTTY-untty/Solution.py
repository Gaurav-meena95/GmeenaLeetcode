s = input()
ans = []
for i in s:
    if i == '#' and ans:
        ans.pop()
    else:
        ans.append(i)
final = ''
for i in ans:
    final += i
print(final)