n = int(input())
arr = list(map(int,input().split()))
s = set()
for i in arr:
    s.add(i)
    
print(*s)