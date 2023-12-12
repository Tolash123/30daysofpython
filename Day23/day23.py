# To create a new object type called sample
class sample:
    pass
# To create instance of sample
x = sample()
print(type(x))

# To initialize attribute of an object
class Dog:
    def __init__(self,breed):
        self.breed = breed

sam = Dog(breed ='Lab')
frank = Dog(breed='Huskie')
print(type(sam))
print(sam)

# creating a class for car
class Car:
    def __init__(car,brand):
        car.brand = brand
dristol = Car(brand ='Limbo')
aeys = Car(brand='limbo')

print(type(dristol))
print(dristol.brand)

# Note: The method above is used to initialize the attributes of an object

class Dog:
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

# creating a circle class
class Circle:
    pi = 3.14
    # Circle gets instantiated with a radius(default is 1)
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    # Method for resetting Radius
    def setRadius(self,new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi
    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2
# changing the radius and see how that affects our Circle object
c = Circle()
c.setRadius(7)
print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

# Inheritance
class Animal:
    def __init__(self):
        print('Animal created')
    def whoami(self):
        print('Animal')
    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    def whoami(self):
        print('Dog')
    def bark(self):
        print('Woof!')

d = Dog()
d.whoami()
d.bark()
print(type(d))
