
a=int(input())

stack=['not']
result=''
j=1

for i in range(a):
    b=int(input())
    while True:
        if b==stack[-1]:
            result+='-\n'
            stack.pop(-1)
            break
        elif j>b:
            result='NO'
            break
        else:
            stack.append(j)
            result+='+\n'
            j+=1
    if result=='NO':
        break
    
print(result)