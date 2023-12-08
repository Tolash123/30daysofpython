# Day-17 of #30daysofpython

## Pattern printing
1. To printsquare pattern with * symbols
n=int(input('Enter No Of Rows:'))
for i in range(n):
    print('* '*n) 

2. print square pattern with digit in every row
n=int(input('Enter No Of Rows:'))
for i in range(n):
    print((str(i+1)+' ')*n)

3. print square pattern with alphabet symbols
n=int(input('Enter No Of Rows:'))
for i in range(n):
    print((chr(65+i)+' ')*n) 
4. Print Right Angle Triangle pattern with + symbols
n=int(input('Enter No Of Rows:'))
for i in range(n):
    for j in range(i+1):
        print('+',end=' ')
    print() 
5. Print Inverted Right Angle Triangle pattern with $ symbol
n=int(input('Enter No Of Rows:'))
for i in range(n):
    print('$ '*(n-i)) 
6. Print Pyramid pattern with + symbols