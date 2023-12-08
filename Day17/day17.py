# To print square pattern with * symbols
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

# Print Inverted Right Angle Triangle pattern with $ symbol
n = int(input('Enter No of rows: '))
for i in range(n):
    print('$ '*(n-i))

# To Print Pyramid pattern with + symbols
n = int(input('Enter No of rows: '))
for i in range(n):
    print(' '*(n-i-1)+(' +')*(i+1))

# Print Inverted Pyramid Pattern with + symbols
n = int(input('Enter No of rows: '))
for i in range(n):
    print(' '*i+' +'*(n-i))

#  Print Diamond Pattern with * symbols
n = int(input('Enter No of rows: '))
for i in range(n):
    print(' '*(n-i-1)+(' +')*(i+1))
for i in range(n):
    print(' '*i+' +'*(n-i))