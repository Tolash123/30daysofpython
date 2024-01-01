print(""" == TODO list App == """)
my_list =[]
def todo():
    print()
    while True:
        todo_list = input('Do you want to view, add or edit: ')
        if todo_list == 'view':
            for item in my_list:
                print(item)
            else:
                pass
        elif todo_list == 'add':
            add = input('Add to your todo app: ')
            my_list.append(add)
        elif todo_list == 'edit':
            my_list.remove(my_list[-1])
todo()


