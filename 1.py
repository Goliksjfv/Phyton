n=10
A=[0]*n
print('vvedite elemnt massiva')
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



FROM python:3.9-slim

WORKDIR /usr/src/app

COPY app.py .

CMD ["python", "app.py"]

