a=int(input())
b=list(map(int,input().split()))


dp=[]
dp2=[0]*a
for i in range(a):
    if i==0:
        dp.append(1)
    else:
        v=0
        for j in range(i):
            if b[i]>b[j] and v<dp[j]+1:
                v=dp[j]+1
        if v==0:
            dp.append(1)
        else:
            dp.append(v)
for i in range(a-1,-1,-1):
    if i==0:
        dp2[i]=1
    else:
        v=0
        for j in range(i,a):
            if b[i]>b[j] and v<dp2[j]+1:
                v=dp2[j]+1
        if v==0:
            dp2[i]=1
        else:
            dp2[i]=v
            
dp3=[dp[i]+dp2[i] for i in range(a)]

print(max(dp3)-1)