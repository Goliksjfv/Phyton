A=str(input())
b=0
for i in range(len(A)):
    if(A[i]=='('):
        b+=1
    if(A[i]==')'):
        b-=1
    if(b<0):
        print('Неправильно')
        exit()
print('Правильно')
exit()
    
    
