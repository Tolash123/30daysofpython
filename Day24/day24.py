# Hands on project
# 1. Create Python class named Student and display its type
class Student:
    def __init__(self):
        pass
s = Student()
print(type(s))

# 2. calling a variable and function by creating a simple class
class Cat:
    def __init__(self):
        print('This is a cat!')
Cat()

# 3. Create a class with one static variable and two instace variables
class Estate:
    s_variable = 'This is a mighty estate'
print(Estate.s_variable)
instance = Estate()
instance.s_variable = 'I love skyscrapers'
print(instance.s_variable)
instance.s_variable = 'I love duplexes'
print(instance.s_variable)

# 4. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
v = Vehicle(246, 18)
print(v.max_speed, v.mileage)

# 5. Create a simple class Person with constructor and one argument name
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is ', self.name)
p = Person('Dristol')
p.say_hi()

# 6. Create a class for Students information like name, rollno, marks and school name with static variable.
class Student:
    def __init__(self, name, rollno, marks, college):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        self.college = college
    def __str__(self):
        print('Name:', self.name, 'Roll-no:', self.rollno, 'Marks:',self.marks, 'college:', self.college )
data = Student('Alade Idris', '1', '98', 'Chicago college')
data1 = Student('Tolani Idris', '1', '98', 'Chicago college')
data2 = Student('Talib Ahmed', '1', '98', 'Chicago college')

data.__str__()
data1.__str__()
data2.__str__()

# 7. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, brand, speed, mileage):
        self.brand = brand
        self.speed = speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
brand = Bus('maybach', 180, 12)
print('Vehicle name:',brand.brand, 'speed:',brand.speed, 'Mileage:',brand.mileage)


# 8. Create a class Employee with two arguments name and salary 
class Employee:
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count +=1
    def displayCount(self):
        print('Total employee %d' %Employee.count)
    def displayEmployee(self):
        print('Name:', self.name, 'salary:', self.salary)
a = Employee('Dr8stol',2000)
b = Employee('Abdul', 5000)
a.displayEmployee()
b.displayEmployee()
print('Total employee: {}'.format(Employee.count))
