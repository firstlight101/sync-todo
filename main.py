
print ("=== Sync Todo ===")

task = []

while True:
    print("1.查看待办事项")
    print("2.添加待办事项")
    print("0.退出")
    oprate = input("请输入选项")
    if(oprate == '0'):
        print("再见")
        break
    elif(oprate == '1'):
        if not task:
            print("暂无待办")
        else:
            for i in task:
                print(i)
    elif(oprate == '2'):
        title = input("待办标题是什么？")
        task.append(title)
        print('添加成功')
    else:
        print("无效选项，请重新输入")