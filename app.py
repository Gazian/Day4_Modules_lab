from data.task_list import *
from modules.output import *
from modules.task_list import *
from modules.input import *
from data.task_list import tasks

# create a menu
def print_menu():
    nl()
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("Q or q: Quit")
    nl()

while (True):
    print_menu()
    option = get_menu_input()
    if (option.lower() == 'q'):
        nl()
        print("Quitting...")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(0.75)
        break
    if option == '1':
        nl()
        print(task_descriptions(tasks))
        take_break()
    elif option == '2':
        nl()
        print(print_uncompleted(tasks))
        take_break()
    elif option == '3':
        nl()
        print(print_completed(tasks))
        take_break()
    elif option == '4':
        nl()
        description = get_description_input()
        print(complete_task_with_description(description, tasks))
        take_break()
    elif option == '5':
        nl()
        time = get_time_taken()
        print(min_time(time, tasks))
        take_break()
    elif option == '6':
        nl()
        description = get_description_input()
        print(print_given_tasks(description, tasks))
        take_break()
    elif option == '7':
        nl()
        description = get_description_input()
        time_taken = get_time_taken()
        task = create_task(description, time_taken)
        print(add_to_list(tasks, task))
        take_break()
    else:
        nl()
        print("Invalid input, choose another option...")
        take_break()
