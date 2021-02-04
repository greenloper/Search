#45

n, m=map(int, input().split())
height=list(map(int, input().split()))
# n, m= 4, 6
# height=[19, 15, 10, 17]

max=max(height)

for j in range(max, 0, -1):
    sum=0
    for h in height:
        if h-j>0:
            sum+=h-j
    if sum>=m:
        print(j)
        break