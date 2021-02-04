#32m

n=int(input())
nList=list(map(int, input().split()))
m=int(input())
mList=list(map(int, input().split()))

nList.sort()
mList.sort()

for i in mList:
    if i in nList:
        print("yes", end=" ")
    else:
        print("no", end=" ")