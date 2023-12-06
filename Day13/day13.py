# Accesing characters in a string Indexing,Slicing
a = "Tolani"
print(a[0])
print(a[-6])
print(a[-1])
print(a[3])

# Program to take input string from keyboard & prints characters index wise
a = input('Enter a name: ')
i = 0
for x in a:
    print('The character at positive index {} and the negative index {} is {} '.format(i, i-len(a),x))
    i = i+1
# slicing
b = 'The cow'
print(b[0:])
print(b[10:])
print(b[2:10])

# Mathematical Operators for Strings
a = 'bola' + 'ji'
print(a)

# comparison operator
a = input('Enter your name : ')
b = input('Enter your name : ')
if a == b:
    print('The name is already existing.')
    
else:
    b = input('Enter another name: ')
c = input('Enter your name : ')
d = input('Enter your name : ')
e = input('Enter your name : ')

print('Name: ',a)
print('Name: ',b)
print('Name: ',c)

# Removing spaces
a = '   Aweda'
b =a.split()
print(b)

# to find string
intro = 'My name is Tolani. I am a Nigerian'
c = intro.find('name')
d = intro.rfind('a Nigerian')
print(c)
print(d)

# index()
string = input('Enter a word: ')
subtring = input('Enter a substring of string: ')
try:
    n= string.index(subtring)
except ValueError:
    print('Subtring not found')
else:
    print('subtring is found')

# replacing a string
a = 'Hi, I am Tolani'
b = a.replace('Hi', 'Hello')
print(b)

# splitting of string
a = 'hello mom!'
b = a.split()
for x in b:
    print(x)

# joining string
a = ['date','month','year']
b = '-'.join(a)
print(b)