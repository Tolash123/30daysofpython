# Day-23 of #30daysofpython

## Classes & Objects

### Objects

Using the class keyword
Creating class attributes
Creating methods in a class
Learning about Inheritance
Learning about Polymorphism
Learning about Special Methods for classes


#### 4 principles of OOP:

- Encapsulation
- Abstraction
- Inheritance
- Polymporphism

### Class

User defined objects are created using the class keyword. The class is a blueprint that defines the nature of a future object. From classes we can construct instances. An instance is a specific object created from a particular class. For example, above we created the object lst which was an instance of a list object.

Let see how we can use class:

> Create a new object type called Sample
  class Sample:
     pass
> Instance of Sample
     x = Sample()
     print(type(x))

- By convention we give classes a name that starts with a capital letter. Note how x is now the reference to our new instance of a Sample class. In other words, we instantiate the Sample class.

Inside of the class we currently just have pass. But we can define class attributes and methods.

##### Attribute

An attribute is a characteristic of an object. A method is an operation we can perform with the object.

For example, we can create a class called Dog. An attribute of a dog may be its breed or its name, while a method of a dog may be defined by a .bark() method which returns a sound.

Let's get a better understanding of attributes through an example.

- Attributes
  The syntax for creating an attribute is:

self.attribute = something

- There is a special method called:

__init__()

This method is used to initialize the attributes of an object. For example:

> class Dog:
    def __init__(self,breed):
        self.breed = breed
        
     sam = Dog(breed='Lab')
     frank = Dog(breed='Huskie')
     (sam)

__main__.Dog
Lets break down what we have above.The special method

__init__() 
is called automatically right after the object has been created:

def __init__(self, breed):
Each attribute in a class definition begins with a reference to the instance object. It is by convention named self. The breed is the argument. The value is passed during the class instantiation.

 self.breed = breed

In Python there are also class object attributes. These Class Object Attributes are the same for any instance of the class. For example, we could create the attribute species for the Dog class. Dogs, regardless of their breed, name, or other attributes, will always be mammals. We apply this logic in the following manner:
> class Dog:
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name