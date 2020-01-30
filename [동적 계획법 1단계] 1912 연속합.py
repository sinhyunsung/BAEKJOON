a=int(input())
b=list(map(int,input().split()))

for i in range(1,a):
    if b[i]>0 and b[i-1]>0:
        b[i]=b[i]+b[i-1]
print(max(b))
        