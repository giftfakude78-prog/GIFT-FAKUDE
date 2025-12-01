class ToDoList:
    def __init__(self):
        self,tasks = []

        def add_tasks(self):
            task = input("Enter a task:")
            self.tasks.append(task)
            print("Task added successfully!")

            def view_task(self):
                if not self.tasks:
                    print("No tasks available!")
                else:
                    print("Your Tasks")
                    for i, task in enumerate(self.tasks, 1):
                        print(f"{i}. {task}")

                def delete_task(self):
                   self.view_tasks()
         try:
             task_number = int(input("Enter task number"))
             if task_number < 1 or task_number > len(self.tasks):
                        print("Invalid task number!")
             else:
              del self.tasks[task_number -1]
              print("Task deleted successfully!")
        except ValueError:
         print("Invalid input")
def update_tasks(self):
    self.view_tasks()
   try:
        task_number = int(input("Enter the task number to update:"))
        if task_number <1 or task_number >len(self.tasks):
            print("Invalid task number!")
        else:
            new_task = input("Enter a new task:")
        self.tasks[task_number - 1] = new_task
        print("Task updated successfully!")
            
 except ValueError:
   print("Invalid input!")

def main():
    todo = ToDoList()
    while True:
        print("\nto-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Update Tasks")
        print(5. "Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.delete_task()
        elif choice == "4":
            todo.update_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice!Please try again.")
            if_name_ == "_main_":
            main()

