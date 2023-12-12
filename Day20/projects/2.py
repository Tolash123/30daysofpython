# Generation generator
n = int(input('Enter the year you were born: '))
        
if n in range(1925,1946):
        print('You are a Traditionalist :) ')
elif n in range(1947,1964):
        print('You are a Baby Boomers :)')
elif n in range(1965,1981):
        print('You are a Generation X (:')
elif n in range(1982,1995):
        print('You are a Milenials :)')
elif n in range(1996,2015):
        print('You are a Generation Z :)')



# Grade Generator
user = input('Enter the test name: ')
max = int(input("What's your max_score?: "))
point = int(input('how many points did you get?: '))
if point in range(90, 100):
    percentage = (point/max)*100
    c = round(percentage)
    print(c, '%')
    print('Grade: A')
elif point in range(80, 90):
    percentage = (point/max)*100
    c = round(percentage)
    print(c,  '%')
    print('Grade: B')
elif point in range(70, 80):
    percentage = (point/max)*100
    c = round(percentage)
    print(c,'%')
    print('Grade: C')
elif point in range(60, 70):
    percentage = (point/max)*100
    c = round(percentage)
    print(c, '%')
    print('Grade: D')
else:
    percentage = (point/max)*100
    c = round(percentage)
    print(c, '%')
    print('Grade: F')
