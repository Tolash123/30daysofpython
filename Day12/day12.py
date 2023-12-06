# using transfer statements break
for i in range(20):
    if i == 7:
        print('Processing Enough')
        break
    print(i)
print('out of the loop')

# To check for item in a cart
cart = [10,20,30,600,40]
for item in cart:
    if item > 500:
        print('Insurance is required for the item')
        break
    print('Processing item: ', item)

cart = [10,20,30,600,40,60,70]
for item in cart:
    if item > 500:
        print('Insurance is required for the item, cannot process')
        continue
    print('Processing item: ', item)

# using pass statement
x = 100
if x>100:
    print('x')
else:
    pass
