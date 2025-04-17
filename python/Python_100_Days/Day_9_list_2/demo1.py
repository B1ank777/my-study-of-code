# 列表的方法
list1=[1,1,2,3,4]
list2=list('abcde')
list3=[2,3,1,5,4]
# append/insert
list1.append(5)
list2.insert(2,'f')
print(list1)
print(list2)

# remove/pop/clear
# 这里remove只删除第一个相同的元素
list1.remove(1)
print(list1)

# del
del list1[0]
print(list1)

# sort
list3.sort()
print(list3)

# reverse
list1.reverse()
print(list1)

# 生成式
list4=[i for i in range(1,100) if i%2==0]
print(list4)

list5=[1,2,3,4,5]
list6=[num**2 for num in list5]
print(list6)

