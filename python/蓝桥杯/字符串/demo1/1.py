str_num = input("请输入数字")
# print(str_num)
# 构建映射字典
d = {"0":"〇","1":"一","2":"二","3":"三","4":"四"}

list1 = []

for i in range(0,len(str_num)):
    list1.append(d[str_num[i]])

str1 = "".join(list1)
print(str1)
# print(len(list1))