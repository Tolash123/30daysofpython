# To print for employee of the month
work_hour = [
    ('Alade',400),
    ('Tolani',300),
    ('Dristol', 600)
]
def employee_check(work_hour):
    current_max = 0
    employee_of_month = ''
    for employee, hours in work_hour:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)

print(employee_check(work_hour))

# Interaction between functions

from random import shuffle
#How to shuffle a list in python
ex = [1,2,3,4,5,6]
print(shuffle(ex)) # This will print none
print(ex)

# simple game
my_list = [' ', '0', '']
def shuffle_list(my_list):
    # take in list, and returned shuffle versioned
    shuffle(my_list)
    return my_list

print(shuffle_list(my_list))

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('pick a number: 0,1,2: ')
    return int(guess)

print(player_guess())

def check_guess(my_list,guess):
    if my_list[guess] == '0':
        print('Correct guess')
    else:
        print('Wrong! Better luck next time')
        print(my_list)

check_guess(my_list,2)

