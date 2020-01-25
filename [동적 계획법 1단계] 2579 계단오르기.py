a=int(input())
b=[]
dp=[]

for i in range(a):
    b.append(int(input()))
    dp.append(0)
dp[0],dp[1],dp[2]=b[0],b[1],b[2]

for i in range(3,a):
    dp[i] = max(dp[i-2] + b[i], dp[i-3] + b[i] + b[i-1])

print(dp)