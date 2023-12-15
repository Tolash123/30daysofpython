# To open a file using python code
file = open('/home/idreesy31/30daysofpython/Day21/name.txt', 'r') 
# Note: always put the file path
# change the file path

#To read a file
a = file.read()
print(a)

# To read the line again we need to reset the index to '0' as follows
# readline( ) method reads line by line, readlines( ) method combines & reads all lines into a list.
a = file.readline()
print(a)

file.seek(0)
file.read()
print(a)

# write() function
c = open('/home/idreesy31/30daysofpython/Day21/dristol.txt', 'w')
print(c) 

# append
c = open('/home/idreesy31/30daysofpython/Day21/dristol.txt', 'a')

# writing to a file
c = open('/home/idreesy31/30daysofpython/Day21/dristol.txt', 'w+')
print(c.write('The pristine school, lagos'))

c.close()  # always do this when you're done with a file

# Appending to a file
file = open('/home/idreesy31/30daysofpython/Day21/dristol.txt', 'a')
my_file = open('/home/idreesy31/30daysofpython/Day21/name.txt', 'a+')
print(my_file.write('\n This is being appended to name.txt'))

# Iterating through a file
for line in open('/home/idreesy31/30daysofpython/Day21/dristol.txt'):
    print(line)

for line in open('/home/idreesy31/30daysofpython/Day21/name.txt'):
    print(line)