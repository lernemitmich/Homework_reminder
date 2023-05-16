
tasks = {}
def add_task():
    task_name = input("Enter task name: ")
    deadline = input("Enter deadline or date: ")
    tasks[task_name] = deadline

def display_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for task, deadline in tasks.items():
            print(f"Task: {task} \t Deadline: {deadline}")

def remove_task():
    task_name = input("Enter the name of the task to remove: ")
    if task_name in tasks:
        del tasks[task_name]
        print("Task removed successfully.")
    else:
        print("Task not found.")


import datetime
import time
def workload_reminder():
    today = datetime.date.today()
    upcoming_tasks = []

    for task, deadline in tasks.items():
        if deadline >= str(today):
            upcoming_tasks.append((task, deadline))

    if not upcoming_tasks:
        print("No upcoming tasks.")
    else:
        print("Upcoming tasks:")
        for task, deadline in upcoming_tasks:
            print(f"Task: {task} \t Deadline: {deadline}")
          
def set_notification_preferences():
    timing = input("Enter notification timing (e.g., '09:00 AM'): ")
    frequency = int(input("Enter notification frequency in minutes: "))

    while True:
        workload_reminder()
        time.sleep(frequency * 60)  # Convert frequency to seconds
        print("\n--- Notification ---")


def menu():
    while True:
        print("\nTask Tracker Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            break
        elif choice == "5":
          workload_reminder()

        else:
            print("Invalid choice. Please try again.")

              


if __name__ == "__main__":
     menu()     

  