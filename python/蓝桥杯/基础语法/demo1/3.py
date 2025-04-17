a = input("请输入起始值")
b = input("请输入比值")
c = input("请输入长度")

a = int(a)
b = int(b)
c = int(c)
list1 = []

for i in range(0,c):
    list1.append(a)
    a = a * b

print(f"{list1[0]},{list1[1]},{list1[2]},{list1[3]},{list1[4]}")

# print(f"{a},{b},{c}")