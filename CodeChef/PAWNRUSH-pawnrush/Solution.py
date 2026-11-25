n = int(input())
ans = 0
if n == 2:
    for  i in range(3,8):
        ans += 1
else:
    for  i in range(n,8):
        ans += 1
print(ans)
    