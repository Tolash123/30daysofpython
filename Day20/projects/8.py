# printing colours

print("If you put")
print("\033[33m", end="") #yellow
print("nothing as the")
print("\033[35m", end="") #purple
print("end character")
print("\033[32m", end="") #green
print("then you don't")
print("\033[0m", end="") #default
print("get odd gaps")
print("\033[36m", end="")
print('The world of dristol')
print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")
print()
# color changing with sep=''
print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")


