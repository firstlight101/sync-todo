
print ("=== Sync Todo ===")

task = []

while True:
    print("1.查看待办事项")
    print("2.添加待办事项")
    print("3.标记完成")
    print("0.退出")
    oprate = input("请输入选项")
    if oprate == '0':
        print("再见")
        break
    elif oprate == '1':
        if not task:
            print("暂无待办")
        else:
            for number,i in enumerate(task, start=1):
                if i['done'] == False:
                    print(number, '[未完成]',i['title'])
                elif i['done'] == True:
                    print(number, '[已完成]', i['title'])
    elif oprate == '2':
        title = input("待办标题是什么？")
        task.append({"title":title, "done": False})
        print('添加成功')
    elif oprate == '3':
        if not task:
            print('暂无待办')
            continue
        try:
            num = int(input("请输入待办编号"))
        except ValueError:
            print('请输入整数编号')
            continue
        if not 1 <= num <= len(task):
            print('编号不存在')
            continue
        task[num - 1]['done'] = True
        print('标记完成')
    else:
        print("无效选项，请重新输入")
