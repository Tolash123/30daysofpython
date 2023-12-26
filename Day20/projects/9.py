import random
import os,time
print('Character Builder')
time.sleep(4)
os.system('clear')
def builder():
    name = input('Name Your Legend: ')
    chr = input('Character Type (Human, Elf, Wizard, Orc): ')
    print('character: ', name ) 
    print('Type: ', chr )  

def health_stat():
    health = random.randint(1,6)*12/2 +10
    return health

def strength_stat():
    strength = random.randint(1,6)*12/2 +12
    return strength
def builder1():
    return builder()
def character():
    print('Character Summary') 
    print('-------------------------')
    print('Health:', health_stat())
    print('Strength:', strength_stat())
    print('May your name go down in Legend...')

builder()
character()
print('\n Your opponent')
builder1()
character()
time.sleep(6)
os.system('clear')

print('⚔️ BATTLE TIME ⚔️')
print('⚔️'*20, end='')
print('\nThe battle begins!')

def round():
    p1 = random.randint(1,50)
    p2 = random.randint(1,50)
    if p1>p2:
        print('Legend1 wins first blow')
        print('Legend2 takes a hit, with 8 damages')
    elif p1==p2:
        print('There is no winner')
    else:
        print('Legend2 wins first blow')
        print('Legend1 takes a hit, with 8 damages')
round()    
time.sleep(5)
os.system('clear')
print('⚔️ BATTLE TIME ⚔️')
print('⚔️'*20, end='')
print('\nRound 2!')
def round1():
    p1 = random.randint(1,50)
    p2 = random.randint(1,50)
    if p1>p2:
        print('Legend1 wins second fight')
        print('Legend2 takes a hit, with 7 damages')
        
    elif p1==p2:
        print('There is no winner')
    else:
        print('Legend2 wins second blow')
        print('Legend1 takes a hit, with 85 damages')
round1()    
time.sleep(5)
os.system('clear')

print('⚔️ BATTLE TIME ⚔️')
print('⚔️'*20, end='')
print('\nThe Final Round!')
def round2():
    p1 = random.randint(1,50)
    p2 = random.randint(1,50)
    if p1>p2:
        print('Legend1 wins second fight')
        print('Legend2 takes a hit, with 7 damages')
    elif p1==p2:
        print('There is no winner')
    else:
        print('Legend2 wins second blow')
        print('Legend1 takes a hit, with 85 damages')
round2()    

print('May your name go down as legend!')