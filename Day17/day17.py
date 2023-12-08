# To printsquare pattern with * symbols
n = int(input('Enter no of rows: '))
for i in range(n):
    print('* '*n)

# print square pattern with digit in every row
n = int(input('Enter no of rows: '))
for i in range(n):
    print((str(i+1)+' ')*n)

# print square pattern with letter in every row
n = int(input('Enter no of rows: '))
for i in range(n):
    print((chr(65+i)+' ')*n)

# Print Right Angle Triangle pattern with + symbols
n=int(input('Enter No Of Rows:'))
for i in range(n):
    for j in range(i+1):
        print('+', end=' ')
    print()