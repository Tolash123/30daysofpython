# for for loop
a = 'Aweda'
for i in a:
    print(i)
for word in a:
    print(word, end='')
print('\n')
# to print letter along side with index

a = 'Tolani'
x = 0
for i in a:
    print('for {} the index character is {}'.format(x,a[x]))
    x += 1

# Program to print numbers in range of 1 and 10 using for loop.

for i in range(0,11):
    print(i, end='')
print('\n')
# To print even numbers in between 0 and 20
for i in range(0,21):
    if i%2 == 0:
        print(i, end='')
print('\n')
# To print odd numbers in between 0 and 20

for i in range(0,21):
    if i% 2 == 1:
        print(i, end='')

print('\n')

# To print sum of numbers in a given list
a = [2,3,4,5,6]
sum = 0
for i in a:
    sum += i
    print('The sum of a is = ', sum)


# using while loop
i = 1
while i<=3:
    print('Hello mom!')
    i += 1
# printing numbers from 1 to 10
i =0
while i<=10:
    print(i)
    i += 1
# printing numbers divisible by 3 between 0 to 20
num = int(input('Enter a number: '))
sum = 0
i = 1
while i<=num:
    sum += i
    i += 1
    print('The sum of num is: ', sum)

# Nested loop
for i in range(3):
    for j in range(2):
        print('Champ!')