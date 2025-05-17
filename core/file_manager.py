# core/file_manager.py
import json
import os

FILE_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_tasks(task_list):
    with open(FILE_PATH, "w") as file:
        json.dump(task_list, file, indent=4)
