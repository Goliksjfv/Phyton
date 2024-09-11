n=10
A=[0]*n
print('Введите элемент массива')
for i in range(n):
    print('A[',i,']=',sep='',end='')
    A[i]=int(input())
for i in range(n):
    print(A[i],end=' ')


print()
max=0
k=0
for i in range(n):
    if ((i+1)%2!=0 and A[i]%3==0 and max<A[i]):
        max=A[i]

print(max)




