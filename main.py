
print ("=== Sync Todo ===")

while True:
    print("1.查看待办事项")
    print("0.退出")
    oprate = input("请输入选项")
    if(oprate == '0'):
        print("再见")
        break
    elif(oprate == '1'):
        print("暂无待办")
    else:
        print("无效选项，请重新输入")