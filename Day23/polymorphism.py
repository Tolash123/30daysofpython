# The four classes of OOP
# polymorphism
class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + 'says Woof'
class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + 'says Meow'
niko = Dog('niko ')
fels = Cat('fels ')
print(niko.speak())
print(fels.speak())

# Different ways to demonstrate polymorphism
#using for loop
for pet in [niko,fels]:
    print(pet.speak())

#using function
def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)

# Using abstract classes and inheritance
class Animal:
    def __init__(self,name):# constructor of the class
        self.name = name  
    def speak(self):
        raise NotImplementedError('Subclass must implement abstract')
    
class Dog(Animal):
    def speak(self):
        return self.name + 'says woof'
class Cat(Animal):
    def speak(self):
        return self.name + 'says Meow!'

fido = Dog('Fido')
isik = Cat('isik ')
print(isik.speak())

# Special Methods
# Finally let's go over special methods. Classes in Python can implement certain operations with special method names. These methods are not actually called directly but by Python specific language syntax. For example let's create a Book class:
class Book:
    def __init__(self,title,author,pages):
        print('A book is created')
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return "Title: %s, author: %s, pages: %s"%(self.title,self.author,self.pages)
    def __len__ (self):
        return self.pages
    def __del__ (self):
        print('A book is destroyed')

book = Book('python Rocks!', 'Jose portilla', 159)
# special methods
print(book)
print(len(book))
del book

# The __init__(), __str__(),__len__(),and __del__() methods
# These special methods are defined by their use of underscores. They allow us to use Python specific functions on objects created through our class.