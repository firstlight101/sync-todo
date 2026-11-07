import json
from pathlib import Path
DATA_FILE = Path(__file__).resolve().parent / "data" / "task.json"

def save_task(task_list):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w",encoding="utf-8") as file:
        json.dump(task_list, file, ensure_ascii=False, indent=2)

def load_task():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []