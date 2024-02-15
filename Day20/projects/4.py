# Character Builder
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

builder()
def character():
    print('Character Summary') 
    print('-------------------------')
    print('Health:', health_stat())
    print('Strength:', strength_stat())
    print('Dexterity: 10')
    print('Intelligence: 10')
    print('Constitution: 10')
    print('Charisma: 10')
    print('May your name go down in Legend...')

character()
while True:
    def new_character():
         ask = input('Do you want to create another character?: ')
         if ask == 'yes':
          return builder(), health_stat(),strength_stat,character()
         else:
            pass
         exit()

    new_character()
