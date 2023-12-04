#Day4

# single input
a = input('Enter your name: ')
print('Name: ',a)

# shortcut to print multiple input
# adding 3 numbers. it can be more than that by changing the codes
a,b,c = [int(x) for x in input('Enter numbers you want to add seperated with commas: ').split(',')]
print('The sum of the number = ', a+b+c)

# to multiply numbers from output
a,b,c = [int(x)for x in input('Enter numbers to be multiplied: ').split(',')]
print('The product of the number = ', a*b*c)

# using eval() functiion
a = eval(input('Enter a word: '))
print(a)
print(type(a))