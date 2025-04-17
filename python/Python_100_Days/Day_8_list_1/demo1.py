# 构造一个从m到n的列表
list1=list(range(2,9))
# 将一个字符串类型的数拆分成一个列表
list2=list('Hello')

print(list1)
print(list2)

# +表示列表的拼接
list3=list(range(10,15))
print(list1+list3)

# *表示列表的重复
print(list1*2)

# 用in和not in表示一个元素在不在列表中
print(3 in list1)
print('a' not in list2)

# list[-1]表示最后一个元素,list[n]表示第一个元素

# 切片,list[start:end:stride]开始,结束,跨度
# 在start等于0,end等于n时,可以省略

# 通过切片来修改
list1[1:3]=[9,10,11]
print(list1)