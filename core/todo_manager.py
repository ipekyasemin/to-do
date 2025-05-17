# core/todo_manager.py
from models.task import Task
from core.file_manager import load_tasks, save_tasks

class ToDoManager:
    def __init__(self):
        self.tasks = [Task.from_dict(t) for t in load_tasks()]

    def add_task(self, title, due_date=None):
        task = Task(title, due_date)
        self.tasks.append(task)
        self.save()

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save()

    def save(self):
        save_tasks([t.to_dict() for t in self.tasks])
