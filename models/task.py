# models/task.py
from datetime import datetime

class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            due_date=data.get("due_date"),
            completed=data.get("completed", False)
        )
