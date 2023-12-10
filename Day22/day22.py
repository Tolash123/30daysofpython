# using try,except and else statement
try:
    f = open('name.txt', 'r')
    f.write('Test write this')
except IOError:
    print('Error: could not find file or read data')
else:
    print('Content written successfully')
    f.close()

# proving the wrong input
def askint():
    while True:
        try:
            val = int(input('Enter an integer:'))
        except:
            print('looks like you did not enter an integer.')
            continue
        else:
            print('Yep that is an integer!')
            print(val)
            break
        finally:
            print('Finally, I executed')  
askint()
