from sqlite_storage import init_db, load_task, insert_task, complete_task



def show_tasks(task_list):
    if not task_list:
        print("暂无待办")
    else:
        for number,i in enumerate(task_list, start=1):
            if i['done'] == False:
                print(number, '[未完成]',i['title'])
            elif i['done'] == True:
                print(number, '[已完成]', i['title'])

def add_task():
    title = input("待办标题是什么？")
    insert_task(title)
    print('添加成功')

def mark_task(task_list):
    if not task_list:
        print('暂无待办')
        return
    try:
        num = int(input("请输入待办编号"))
    except ValueError:
        print('请输入整数编号')
        return
    if not 1 <= num <= len(task_list):
        print('编号不存在')
        return
    task_id = task_list[num-1]["id"]
    complete_task(task_id)
    print('标记完成')


def main():
    init_db()
    while True:
        task = load_task()
        print ("=== Sync Todo ===")
        print("1.查看待办事项")
        print("2.添加待办事项")
        print("3.标记完成")
        print("0.退出")
        oprate = input("请输入选项")
        if oprate == '0':
            print("再见")
            break
        elif oprate == '1':
            show_tasks(task)
        elif oprate == '2':
            add_task()
        elif oprate == '3':
            mark_task(task)
        else:
            print("无效选项，请重新输入")

if __name__ == "__main__":
    main()

