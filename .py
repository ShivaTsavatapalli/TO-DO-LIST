class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

    def mark_task_as_done(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
        else:
            print("Invalid task number.")

def main():
    todo_list = Todo()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as done: "))
            todo_list.mark_task_as_done(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
