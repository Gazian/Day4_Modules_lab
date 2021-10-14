import time

def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

# 3. Print a list of all task descriptions
def task_descriptions(tasks):
    descriptions = []
    for task in tasks:
        descriptions.append(task["description"])
    return descriptions

# break and format after functions called
def take_break():
    print("")
    time.sleep(2)

# bigger menu break
def menu_break():
    print("")
    print("")
    time.sleep(4)

# new line
def nl():
    print("")
