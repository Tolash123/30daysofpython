# list 
a = [1,2,3,4,5]
print(type(a))
print(len(a))
print(max(a))
print(min(a))

l = []
for i in a:
    l += [i]
    print(l)

###
objects = [1,'book']
objects.append(['bag', 'yellow'])
objects.extend([1,2,3])
objects.insert(2,['club'])
print(objects)
print(objects[4])

# sorting list
name = ['Alade', 'Toheeb', 'Habeeb', 'Ayo']
name.sort()
sorted(name)
print(name)

# Sorting in Descending order
l = [0,5,8,3,2,7]
l.sort(reverse = True)
print(l)


# counting repeated elements
a = [1,1,2,2,4,2,2,2,2,2,2,3,3,3]
print(a.count(2))
print(a.index(4))

# To join
l = ['Hi','Balaji!','How','are','you','?']
a = ' '.join(l)
print(a)

student = []
name = input('Enter your name: ')
student.append(name)
print (student)

