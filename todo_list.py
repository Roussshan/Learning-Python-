# Beginner-friendly To-Do List App
# This program helps you add, view, mark complete, and remove tasks.

# Create an empty list to store tasks
tasks = []


def add_task():
    """Add a new task to the list."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty.")
        
def view_tasks():
    """Show all tasks in the list."""
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
