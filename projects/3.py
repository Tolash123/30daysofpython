def even_list(num):
    even_num = []
    # Go through each number
    for n in num:
        # if the output is True
        if n % 2==0:
            even_num.append(n)
            print(even_num)
        else:
            pass
        
print(even_list([1,2,3,4,6,7]))