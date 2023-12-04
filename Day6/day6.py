# Car Price based on brand
brand = input('Enter the car brand : ').upper()
if brand == 'bmW'.upper():
    print('The price of {} is 2 million'.format(brand))
elif brand == 'maybacH'.upper():
    print('The price of {} is 250 million'.format(brand))
elif brand == 'toyota'.upper():
    print('The price of {} is 250 million'.format(brand))
elif brand == 'rollsroyce'.upper():
    print('The price of {} is 250 million'.format(brand))
else:
    print('Sorry! We do not have the product you are looking for')
    print('These are the available cars: bmw, maybach, toyota and rollsroyce')

# Program to find biggest of two numbers?

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
if num1>num2:
    print('{} is greater than {}'.format(num1,num2))
elif num1<num2:
    print('{} is greater than {}'.format(num2,num1))
else:
    print(num1 == num2)

# Program to check whether given number is in between 1 & 100
a = int(input('Enter a number in the ranger of 1-100: '))
if a in range(0,101):
    print('{} is present'.format(a))
else:
    print('The number is not in the specified range')

