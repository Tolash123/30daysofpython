import math as m
# assigning value to  variables
a = 15
b = 40
a -= 50
b += 20
print(a)
# terenary operator
x = 30
y = 40
z = x if x < y else y
print(z)

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = a if (a>b and a>c) else b if b>a and b>c else c
print("The highest of three numbers is : ",d)

# special operator
name = ['Alade', 'Tolani', 'Dristol', 'Ayo']
student = input('Enter your name: ')
if(student in name):
    print('The name is existing')
else: 
    print('no such name \n')

# Operator precedence
a = (2+5)*3/2
print(a)

#math module
print(m.sqrt(16))
print(m.pi)
print(m.e)

