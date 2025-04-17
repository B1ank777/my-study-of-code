import random
money=1000

while money>0:
    print(f"你的总资产为{money}")
    # 我要保证输入的金额是符合规范的
    while True:
        debt = int(input("请输入你要加入的赌注:"))
        if 0<debt<=money:
            break

    # 开始摇骰子
    first_point=random.randrange(1,7)+random.randrange(1,7)
    if first_point==7 or first_point==11:
        print("玩家胜!\n")
        money+=debt
    elif first_point==2 or first_point==3 or first_point==12:
        print("庄家胜!\n")
        money-=debt
    else:
        while True:
            current_point=random.randrange(1,7)+random.randrange(1,7)
            if current_point==7:
                print("庄家胜!\n")
                money-=debt
                break
            elif current_point==first_point:
                print("玩家胜!\n")
                money+=debt
                break
print("破产了!\n")
