# Converting cases of a string upper(),lower(),title(),capitalize()

car = 'my favorite car is maybacH'
print(car.upper())
print(car.lower())
print(car.title())
print(car.swapcase())
print(car.capitalize())

# Checking Starting and Ending Part of the String

car = 'my favorite car is maybacH'
print(car.startswith('my')) # this prints true
print(car.endswith('corolla')) # this prints false

# Checking Type of Characters Present in a String
a = 'Dristol01'
print(a.isalnum())
print(a.isdigit())