tasks = []

def display_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Quit")

def add_task():
    tasks.append(input("Enter task: "))

def view_tasks():
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks to view.")

def delete_task():
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            print(f"Deleted: {tasks.pop(task_num - 1)}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def run():
    print("Welcome to the To-Do List!")
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1': add_task()
        elif choice == '2': view_tasks()
        elif choice == '3': delete_task()
        elif choice == '4': break
        else: print("Invalid option.")

if __name__ == "__main__":
    run()