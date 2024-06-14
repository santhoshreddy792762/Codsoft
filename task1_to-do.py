#to-do list application using python

class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        return self.description + (" (DONE)" if self.is_done else "")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def mark_task_as_done(self, task_number):
        self.tasks[task_number - 1].mark_as_done()

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")


def main():
    todo_list = ToDoList()
    while True:
        print("to-do list")
        print("\n1. Add task")
        print("2. Mark task as done")
        print("3. show all tasks")
        print("4. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter your task : ")
            todo_list.add_task(task)
        elif choice == "2":
            task_number = int(input("Enter task number to mark as done: "))
            todo_list.mark_task_as_done(task_number)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
