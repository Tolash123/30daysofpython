import random

greeting =['Ekaro','Hola','Zdravstvuyte','Nǐn hǎo','Salve','Namaste','Shalom','Shikamoo','Bonjour']
num = random.randint(0,8)
print(greeting[num])
import os,time
def pretty():
    import os,time
    os.system('clear')
    print(""" == TODO list App == """)

def todo():
    print(""" == TODO list App == """)
    print()
    my_list =[]
    print()
    while True:
        todo_list = input('Do you want to view, add, delete or edit: ')
        if todo_list == 'view':
            for item in my_list:
                print('-',item)
            else:
                pass
            time.sleep(2)
            pretty()
        elif todo_list == 'add':
            add = input('Add to your todo app: ')
            my_list.append(add)
            pretty()
        elif todo_list == 'delete':
            add = input('Item to be deleted: ')
            if add not in my_list:
                print('The item is not available')
                pretty()
            else:
                print('The item is available')

            delete = input('Are you sure you want to delete:')
            if add in my_list and delete == 'yes':
                 my_list.remove(add)
            elif add not in my_list:
                pass
            else:
                pass 
            pretty()
        elif todo_list == 'edit':
            add = input('Item to be edited: ')
            if add not in my_list:
                print('The item is not available')
                pretty()
            else:
                print('The item is available')

            edit = input('Are you sure you want to edit:')
            if add in my_list and edit == 'yes':
                 my_list.replace(add,add)
            elif add not in my_list:
                pass
            else:
                pass 
            pretty()
            

todo()


