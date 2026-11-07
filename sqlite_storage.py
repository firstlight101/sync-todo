import sqlite3
from pathlib import Path

DB_file = Path(__file__).resolve().parent / "data" / "task.db"

def init_db():
    DB_file.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_file)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
        )   
    """)

    connection.commit()
    connection.close()

def insert_task(title):
    connection = sqlite3.connect(DB_file)

    connection.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    connection.commit()
    connection.close()

def load_task():
    connection = sqlite3.connect(DB_file)

    cursor = connection.execute(
        "SELECT id, title, done FROM tasks ORDER BY id"
    )
    rows = cursor.fetchall()
    connection.close()
    task_list = []
    for task_id, title, done in rows:
        task_list.append({
            "id": task_id,
            "title": title,
            "done": bool(done)
        })
    return task_list

def complete_task(task_id):
    connection = sqlite3.connect(DB_file)

    connection.execute(
        "UPDATE tasks SET done = 1 WHERE id = ?",
        (task_id,)
    )
    connection.commit()
    connection.close()

if __name__ == "__main__":
    init_db()
    rows = load_task()
    for row in rows:
        print(row)
    # title = input("请输入待办标题")
    # insert_task(title)
    # print("已添加至数据库")
