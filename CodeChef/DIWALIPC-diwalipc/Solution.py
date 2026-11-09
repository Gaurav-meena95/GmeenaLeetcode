t = int(input())
for _ in range(t):
    p,d,k,b = map(int,input().split())
    expected = p + (d * k)
    if expected <= b:
        print('YES')
    else:
        print ('NO')
        