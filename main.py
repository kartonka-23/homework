from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not done"
        return f"{self.title} | {self.description} | Deadline: {self.deadline} | {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()

    def list_tasks(self):
        for task in self.tasks:
            print(task)


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Math Homework", "Solve exercises 1-10", "2025-04-12")
    manager.add_task("Buy groceries", "Milk, Bread, Eggs", "2025-04-11")
    manager.list_tasks()
    manager.mark_task_completed("Math Homework")
    manager.list_tasks()