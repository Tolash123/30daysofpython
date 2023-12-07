s = 'abcdefghij'
print(s[1:6:2])

print(s[::1])
print(s[::-1])
print(s[3:7:-1]) # Returns empty because in backward direction, we can't go from 3 to 8

print(s[7:4:-1])
print(s[0:100000:1])
print(s[-4:1:-1])
print(s[-4:1:-2])
print(s[5:0:1]) # Returns empty string because in forward direction if end is '0'

print(s[-5:0:1])
# print(s[9:0:0])  #Gives value error because step value cannot be zero


print(s[0:-10:-1])
print(s[0:-11:-1])
print(s[0:0:]) # In forward direction, end shouldn't be empty
print(s[0:-9:-2])
print(s[-5:-9:-2])
print(s[10:-1:-1])
print(s[10000:2:-1])
