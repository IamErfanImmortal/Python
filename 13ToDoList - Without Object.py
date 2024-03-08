tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added successfully.')

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed successfully.')
    else:
        print(f'Task "{task}" not found in the list.')

def search_task(keyword):
    matching_tasks = [task for task in tasks if keyword.lower() in task.lower()]
    if matching_tasks:
        print(f'Tasks containing "{keyword}":')
        for task in matching_tasks:
            print(f' - {task}')
    else:
        print(f'No tasks containing "{keyword}" found.')

def display_all_tasks():
    if tasks:
        print("All tasks:")
        for task in tasks:
            print(f' - {task}')
    else:
        print("No tasks available.")

def display_menu():
    print("\n===== ToDo List Menu =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Search Tasks by Keyword")
    print("4. Display All Tasks")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        keyword = input("Enter the keyword to search: ")
        search_task(keyword)
    elif choice == "4":
        display_all_tasks()
    elif choice == "5":
        print("Exiting the ToDo List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
