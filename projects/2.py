import cmath as m
#quadratic formula
a = 1
b = 2
c = 5
d = (b**2) - (4*a*c)

root1 = (-b+m.sqrt(d))/2*a
root2 = (-b-m.sqrt(d))/2*a
print(root1)
print(root2)

print('Welcome! We can help you solve your quadratic equation. \n')

a = int(input('Enter the value for a: '))
b = int(input('Enter the value for b: '))
c = int(input('Enter the value for c: '))

def quadratic_formula(a,b,c):
    d = (b**2) - (4*a*c)

root3 = (-b+m.sqrt(d))/2*a
root4 = (-b-m.sqrt(d))/2*a
print(root3)
print(root4)

