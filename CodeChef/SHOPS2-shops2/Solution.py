t = int(input())
for _ in range(t):
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    vist1 = d + sum(arr)
    vist2 = d + sum(brr)
    both = 2 * d 
    for i in range(n):
        both += min(arr[i],brr[i])
    print(min(vist2,vist1,both))