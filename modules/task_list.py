# MVP
# 1. Print a list of uncompleted tasks
def print_uncompleted(tasks):
    uncompleted = []
    for task in tasks:
        if task["completed"] == False:
            uncompleted.append(task["description"])
    return uncompleted

# 2. Print a list of completed tasks
def print_completed(tasks):
    completed = []
    for task in tasks:
        if task["completed"] == True:
            completed.append(task["description"])
    return completed

# 3. Print a list of all task descriptions
def task_descriptions(tasks):
    descriptions = []
    for task in tasks:
        descriptions.append(task["description"])
    return descriptions

## Refactor get_uncompleted_tasks and get_completed_tasks
def get_tasks_by_status(list, status):
    tasks = []
    for task in list:
        if task["completed"] == status:
            tasks.append(tasks)
    return tasks

# 4. Print a list of tasks where time_taken is at least a given time
def min_time(time, tasks):
    long_tasks = []
    for task in tasks:
        if task["time_taken"] >= time:
            long_tasks.append(task["description"])
    if len(long_tasks) == 0:
        return "No tasks over or equal to that time."
    return long_tasks

# 5. Print any task with a given description
def print_given_tasks(description, tasks):
    for task in tasks:
        if task["description"].lower() == description.lower():
            return task
    return "Task not in list."

# 7. Add a task to the list
def create_task(task_description, task_time):
    task = {}
    task["description"] = task_description
    task["completed"] = False
    task["time_taken"] = task_time
    return task

# add a task to the list
def add_to_list(list, task):
    list.append(task)
    return "Added task to list."

# find task in list from description and mark as compelte
def complete_task_with_description(description, list):
    for element in list:
        if description.lower() == element["description"].lower():
            element["completed"] = True
            return "Task marked as complete."
    return "Task not found in list."
        