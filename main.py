import sys
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# File used to persist task data
FILE: str = "tasks.json"

def load_tasks() -> List[Dict]:
    """
    Load tasks from the JSON file.

    Returns:
        List[Dict]: A list of task dictionaries.
        Returns an empty list if the file does not exist.
    """
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks: List[Dict]) -> None:
    """
    Save the given list of tasks to the JSON file.

    Args:
        tasks (List[Dict]): List of task objects to save.
    """
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description: str) -> None:
    """
    Add a new task to the task list.

    Args:
        description (str): The task description.
    """
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def list_tasks(filter_status: Optional[str] = None) -> None:
    """
    List all tasks, optionally filtered by status.

    Args:
        filter_status (Optional[str]): Filter by task status ('todo', 'done', 'in-progress').
    """
    tasks = load_tasks()
    for task in tasks:
        if not filter_status or task["status"] == filter_status:
            print(f"[{task['id']}] {task['description']} - {task['status']}")

def update_task(task_id: int, new_desc: str) -> None:
    """
    Update the description of a task.

    Args:
        task_id (int): The ID of the task to update.
        new_desc (str): The new description for the task.
    """
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["description"] = new_desc
            t["updatedAt"] = datetime.now().isoformat()
            break
    save_tasks(tasks)

def delete_task(task_id: int) -> None:
    """
    Delete a task by ID.

    Args:
        task_id (int): The ID of the task to delete.
    """
    tasks = [t for t in load_tasks() if t["id"] != task_id]
    save_tasks(tasks)

def mark_status(task_id: int, new_status: str) -> None:
    """
    Change the status of a task.

    Args:
        task_id (int): The ID of the task to update.
        new_status (str): The new status (e.g. 'done', 'in-progress').
    """
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = new_status
            t["updatedAt"] = datetime.now().isoformat()
            break
    save_tasks(tasks)

def main() -> None:
    """
    Main CLI entry point.
    Parses command-line arguments and executes the corresponding command.
    """
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        print("Commands: add, list, update, delete, mark-done, mark-in-progress")
        return
        
    cmd = sys.argv[1]
    
    match cmd:
        case "add":
            if len(sys.argv) < 3:
                print("Error: 'add' command requires a description.")
            else:
                description = " ".join(sys.argv[2:])
                add_task(description)
                
        case "list":
            filter_status = sys.argv[2] if len(sys.argv) > 2 else None
            list_tasks(filter_status)
            
        case "update":
            if len(sys.argv) < 4:
                print("Error: 'update' requires an ID and a new description.")
            else:
                try:
                    task_id = int(sys.argv[2])
                    new_desc = " ".join(sys.argv[3:])
                    update_task(task_id, new_desc)
                    print(f"Task {task_id} updated.")
                except ValueError:
                    print("Error: Task ID must be an integer.")
                    
        case "delete":
            if len(sys.argv) < 3:
                print("Error: 'delete' requires a task ID.")
            else:
                try:
                    task_id = int(sys.argv[2])
                    delete_task(task_id)
                    print(f"Task {task_id} deleted.")
                except ValueError:
                    print("Error: Task ID must be an integer.")
        
        case "mark-done" | "mark-in-progress":
            if len(sys.argv) < 3:
                print(f"Error: '{cmd}' requires a task ID.")
            else:
                try:
                    task_id = int(sys.argv[2])
                    status_value = cmd.split('-')[1]
                    mark_status(task_id, status_value)
                    print(f"Task {task_id} marked as {status_value}.")
                except ValueError:
                    print("Error: Task ID must be an integer.")
                    
        case _:
            print(f"Error: Unknown command '{cmd}'.")

if __name__ == "__main__":
    main()
