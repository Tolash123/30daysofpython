# Dictionary
ex = {1:'a', 2:'b', 3:'c', 4:'d'}
print(ex)
print(type(ex))
print(len(ex))
print(str(ex))
print(ex.keys())
print(ex.values())
print(ex.items())
print(ex.get(2))
print(ex.setdefault(4))

# method: adding elements in dictionary
name = {'Alade', 'Tolani', 'Abdul'}
student = {'Aweda'}
name.update(student)
print(sorted(name))
print(type(name))

# using fromkeys
x1 = ('k-1', 'k-2', 'k-3','k-4')
x2 = 'Tolani'
d1 =  {}
d2 = d1.fromkeys(x1,x2)
print(d2)
d3 = d2.copy()
print(d3)