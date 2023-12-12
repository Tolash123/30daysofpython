# program that loops
animal = input('What animal do you want?:')
while True:
    if animal == 'Cow':
        print('A cow goes moo.')
        continue
    elif animal == 'Lemur':
        print('Ummm...the Lesser Spotter Lemur goes awooga.')
    elif animal == 'A Lesser Spotted lemur':
        print('Ummm...the Lesser Spotter Lemur goes awooga.')
    else:
        print('I dont know that animal.')
    exit()

