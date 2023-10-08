class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Great! I've added '{task}' to your to-do list.")

    def view_tasks(self):
        if self.tasks:
            print("Here's your to-do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is currently empty. Time to get productive!")

    def update_task(self, task_index, new_task):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task
            print(f"Task {task_index} has been updated to '{new_task}'.")
        else:
            print("Oops! That task doesn't exist in your list.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task {task_index} '{removed_task}' has been successfully removed.")
        else:
            print("Sorry, there's no task at that index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new task")
        print("2. View your tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            task = input("What's the new task you want to add? ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number you want to update: "))
            new_task = input("What should it be updated to? ")
            todo_list.update_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task number you want to delete: "))
            todo_list.delete_task(task_index)
        elif choice == '5':
            print("Thanks for using the To-Do List Manager. Have a productive day!")
            break
        else:
            print("Oops! That's not a valid option. Please choose a valid number.")

if __name__ == "__main__":
    main()
