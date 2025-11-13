# 📝 Task CLI Manager

A lightweight **command-line task manager** built with pure Python — no external dependencies required.  
It stores tasks locally in a JSON file and allows adding, listing, updating, deleting, and marking tasks with different statuses.

---

## ⚙️ Features

- Add new tasks with descriptions  
- List all tasks or filter by status (`todo`, `done`, `in-progress`)  
- Update or delete existing tasks  
- Mark tasks as done or in progress  
- Data is persisted locally in a simple JSON file  
- **No external dependencies required**

---

## 📁 Project Structure

```
task_cli/
├── task_cli.py
└── tasks.json  # auto-created after first run
```

---

## 🚀 How to Run

### 1. Clone the repository (or copy the file)

```bash
git clone https://github.com/manuelmslv/task-cli-manager.git
cd task-cli-manager
```

### 2. Run the script

Make sure you have **Python 3.10+** installed, then execute:

```bash
python task_cli.py <command> [arguments]
```

---

## 🧩 Commands

| Command | Description | Example |
|----------|--------------|----------|
| `add` | Add a new task | `python task_cli.py add "Finish the report"` |
| `list` | List all tasks | `python task_cli.py list` |
| `list <status>` | List tasks filtered by status | `python task_cli.py list done` |
| `update <id> <new description>` | Update task description | `python task_cli.py update 2 "Write documentation"` |
| `delete <id>` | Delete a task by ID | `python task_cli.py delete 1` |
| `mark-done <id>` | Mark task as done | `python task_cli.py mark-done 3` |
| `mark-in-progress <id>` | Mark task as in progress | `python task_cli.py mark-in-progress 4` |

---

## 📦 Data Storage

All tasks are stored in a local file called `tasks.json`.  
Example structure:

```json
[
    {
        "id": 1,
        "description": "Finish project report",
        "status": "todo",
        "createdAt": "2025-11-10T10:35:00",
        "updatedAt": "2025-11-10T10:35:00"
    }
]
```

---

## 🧠 Code Overview

### Main Components

| Function | Purpose |
|-----------|----------|
| `load_tasks()` | Loads all tasks from `tasks.json`. |
| `save_tasks(tasks)` | Saves the given list of tasks. |
| `add_task(description)` | Adds a new task to the list. |
| `list_tasks(filter_status)` | Displays tasks (optionally filtered). |
| `update_task(task_id, new_desc)` | Updates the description of a specific task. |
| `delete_task(task_id)` | Deletes a task by ID. |
| `mark_status(task_id, new_status)` | Updates the status of a specific task. |

---

## 🧩 Example Usage

```bash
# Add new tasks
python task_cli.py add "Prepare presentation"
python task_cli.py add "Write project summary"

# List all tasks
python task_cli.py list

# Mark a task as done
python task_cli.py mark-done 1

# List only completed tasks
python task_cli.py list done

# Update a task
python task_cli.py update 2 "Write project documentation"

# Delete a task
python task_cli.py delete 1
```

---

## 💡 Notes

- All data is persisted automatically — you don’t need a database.
- The script is completely **standalone** and requires only Python’s standard library.
- To reset your data, simply delete the `tasks.json` file.

---

## 🧾 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it as you wish.

---

## 👨‍💻 Author

**Manuel Monsalve**  
[GitHub: manuelmslv](https://github.com/manuelmslv)
