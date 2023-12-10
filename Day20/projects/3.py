def askint():
    try:
        val = int(input('Enter an integer:'))
    except:
        print('looks like you did not enter an integer.')
    finally:
        print('Finally, I executed')
    print(val)
askint()