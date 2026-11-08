import flet as ft
from sqlite_storage import init_db, load_task, insert_task, complete_task

def main(page: ft.Page):
    page.title = "Sync Todo"
    page.add(ft.Text("我的待办", size = 24))

    title_input = ft.TextField(label="待办标题")
    result_text = ft.Text()
    task_column = ft.Column()
    def refresh_tasks():
        task_column.controls.clear()
        task_list = load_task()

        if not task_list:
            task_column.controls.append(ft.Text("暂无待办"))
            return

        for item in task_list:
            if item["done"]:
                task_column.controls.append(
                    ft.Text("[已完成]"+item["title"])
                )
                continue
            button = ft.Button(
                "标记完成",
                data = item["id"],
                on_click=mark_clicked
            )
            row = ft.Row(controls=[
                ft.Text("[未完成]" + item["title"], expand=True),
                button
            ])
            task_column.controls.append(row)


    def mark_clicked(e):
        task_id = e.control.data
        complete_task(task_id)
        result_text.value= "标记完成"
        refresh_tasks()
        page.update()
    
    def add_clicked(e):
        title = title_input.value.strip()

        if not title:
            result_text.value = "请输入待办标题"
            page.update()
            return
        
        insert_task(title)
        title_input.value = ''
        result_text.value = "添加成功"
        refresh_tasks()
        page.update()

    page.add(
        title_input,
        ft.Button("添加", on_click=add_clicked),
        result_text,
        task_column
    )

    init_db()
    refresh_tasks()
    page.update()

if __name__ == "__main__":
    ft.run(main)