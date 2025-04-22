import json
from datetime import datetime

tasks = []


def load_task(filename='task.json'):
        global tasks
        try:
                with open(filename, 'r') as f:
                        tasks = json.load(f)
                except FileNotFoundError:
                        tasks=[]
def save_tasks(filename='task.json'):
        with open(filename,'w') as f:
                json.dump(tasks,f, indent=4)

def add_task(task):
        task_obj = {
                'description': task,
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
        tasks.append(task_obj)
        save_task()
def list_tasks():
        if not tasks:
                print("No tasks yet!")
        for indx, task in enumerate(tasks):
                print(f"{idx + 1}. {task['description']}(added {task['created_at']})")

def delete_task(index):
        if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Deleted: {removed['description']}")
                save_tasks()
        else:
                print("Invalid index")

def main():
    load_tasks()
    while True:
        print("\nCommands: add / list / delete / exit")
        cmd = input("Enter command: ").strip().lower()

        if cmd == 'add':
            task = input("Enter task: ")
            add_task(task)
        elif cmd == 'list':
            list_tasks()
        elif cmd == 'delete':
            try:
                idx = int(input("Enter task number to delete: ")) - 1
                delete_task(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif cmd == 'exit':
            print("Bye!")
            break
        else:
            print("Unknown command.")
if __name__ == "__main__":
    main()
