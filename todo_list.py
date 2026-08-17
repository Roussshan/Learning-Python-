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

def mark_done():
    """Mark a task as completed by removing it from the list."""
    if not tasks:
        print("No tasks to mark complete.")
        return

    view_tasks()
    choice = input("Enter the number of the task you completed: ")

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            completed_task = tasks.pop(index)
            print(f"Great job! You've completed: {completed_task}")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

def remove_task():
    """Remove a task from the list."""
    if not tasks:
        print("There are no tasks to remove.")
        return
