N = input("请输入一个三位数: ")

for i in range(150,int(N) + 1):
    a = i//100
    b = i//10%10
    c = i%10
    if i == a**3 + b**3 + c**3:
        print(i)