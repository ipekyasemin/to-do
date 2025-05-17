# utils/helpers.py
from datetime import datetime

def format_task(task, index):
    status = "✓" if task.completed else "✗"
    return f"{index + 1}. [{status}] {task.title} (Tarih: {task.due_date or 'Belirtilmedi'})"
