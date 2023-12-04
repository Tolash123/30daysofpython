a,b,c = 10,20,30
print('The value of a,b,c are : ', a,b,c)

# To print in a single line using end()
a = [1,2,3,4,5,6,7, '\n']
for i in a:
    print(i, end = '')

# to print on seperate lines
a = [10,20,30,40,50]
for i in a:
    print(i)

# using sep='' attribute
print('10','11','2023', sep='-')
print('Alade', 'is','a', 'good', 'boy', sep='-')

# Using end( ) and sep( ) in a single line

print(10,12,2023,sep=':',end=' December \n')

# print( ) statement with replacemenet operator {}

a = input('Enter your name: ')
b = 'Hello'
print("{} {}!,how are you?".format(a,b))

Name = input('Enter your name: ')
Age  =  21
Goal = 'Data Scientist'
print("Hello {}, your age is {}, your goal is to become a {}".format(Name,Age,Goal))

# Replacement Operator based on Index / a,b,c can also be used in indexing
Age  =  21
Goal = 'Data Scientist'
Name = 'Balaji'
print("Hello {2}, your age is {1}, your goal is to become a {0}".format(Goal,Age,Name))

# print with formatted string

a = 10
print("Value of a : %i"%a)