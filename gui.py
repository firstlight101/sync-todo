import flet as ft
from sqlite_storage import init_db, load_task

def main(page: ft.Page):
    page.title = "Sync Todo"
    page.add(ft.Text("我的待办", size = 24))

    init_db()
    task_list = load_task()

    if not task_list:
        page.add(ft.Text("暂无待办"))

    for item in task_list:
        if item["done"]:
            status = "[已完成]"
        else:
            status = "[未完成]"

        page.add(ft.Text(status + ' ' + item["title"]))

if __name__ == "__main__":
    ft.run(main)