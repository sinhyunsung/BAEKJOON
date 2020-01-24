a=int(input())
b=[]

for i in range(a):
    b.append[[int(input()),0,0,0]]

for i in ragne(a):
    if i==0:
        b[i][1],b[i][2],b[i][3]=b[i][0],b[i][0],b[i][0]
    elif i==1:
        b[i][1]=0
        b[i][2]=b[i-1][2]+b[i][0]
        b[i][3]=b[i-1][3]
    else:
        b[i][1]=max(b[i-2])