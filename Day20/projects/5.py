# Creating class for a rectangle
class Rect:
    def __init__(self,length=10,breadth=5):
        self.length= length
        self.breadth= breadth
        self.perimeter= 2*(length+breadth)
        self.area= length * breadth
r = Rect()
print(r.area)
print(r.perimeter)
print(type(r))

# Creating a class for an Estate and inheritance House
class Estate:
    land = 1550.0
    def __init__(self,skyscrapers=5,duplex=4,storey=3,capacity=3):
        self.skyscrapers = skyscrapers * Estate.land * capacity
        self.duplex = duplex * Estate.land * capacity
        self.storey = storey * Estate.land * capacity
class Housing:
    def __init__(self):
        Estate.__init__(self)
        print('Welcome to our estate.')

    
d = Estate()
e = Housing()
print(e)
print('The price of skyscrapers is: ', d.skyscrapers, '£')
print('The price of duplex is: ', d.duplex, '£')
print('The price of storey is: ', d.storey, '£')

