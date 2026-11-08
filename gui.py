import flet as ft
from sqlite_storage import init_db, load_task, insert_task, complete_task, delete_task, update_task_title

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
            button_edit = ft.Button(
                "编辑标题",
                data = {"id":item["id"], "title":item["title"]},
                on_click=edit_clicked
            )
            button_delete = ft.Button(
                "删除",
                data = item["id"],
                on_click=delete_clicked
            )
            button_mark = ft.Button(
                "标记完成",
                data = item["id"],
                on_click=mark_clicked
            )
            if item["done"]:
                row = ft.Row(controls=[
                    ft.Text("[已完成]" + item["title"], expand = True),
                    button_edit,
                    button_delete
                ]
                )
            else:
                row = ft.Row(controls=[
                    ft.Text("[未完成]" + item["title"], expand=True),
                    button_edit,
                    button_mark,
                    button_delete
                ])
            task_column.controls.append(row)

    def delete_clicked(e):
        task_id = e.control.data
        delete_task(task_id)
        result_text.value = "删除完成"
        refresh_tasks()
        page.update()


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

    def edit_clicked(e):
        task_id = e.control.data["id"]
        task_title = e.control.data["title"]
        new_task_title = ft.TextField(task_title,)

        def save_edited_data(e):
            title = new_task_title.value.strip()
            if not title:
                new_task_title.value = ''
                new_task_title.error="请输入待办标题"
                page.update()
                return
            update_task_title(task_id, new_task_title.value)
            result_text.value = "修改成功"
            page.pop_dialog()
            refresh_tasks()
            page.update()

        dialog = ft.AlertDialog(
            title = ft.Text("修改标题"),
            content= new_task_title,
            actions=[
                ft.Button(
                    "保存", 
                    on_click = save_edited_data
                ),
                ft.Button(
                    "取消",
                    on_click = lambda e: page.pop_dialog()
                )
            ]
        )
        page.show_dialog(dialog)

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