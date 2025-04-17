s=input("请输入一个字符串,要求长度大于等于3:")

# 将s与一个列表对应起来,列表的索引就是s对应索引的字符,初始化列表都为0
list_to_s=[]
for _ in range(len(s)):
    list_to_s.append(0)

# 总遍历
for _ in range(2**64):
    s_last = s
    # 开始操作,一次遍历三个
    for i in range(len(s)-2):
        # if((s[i+1]==s[i] and s[i+1]!=s[i+2]) or (s[i+1] != s[i] and s[i+1]==s[i+2])):
        if s[i+1]==s[i] and s[i+1]!=s[i+2]:
            list_to_s[i+1]=1
            list_to_s[i+2]=1
        if s[i+1] != s[i] and s[i+1]==s[i+2]:
            list_to_s[i+1]=1
            list_to_s[i]=1

    i=0
    # 已经标记完所有的边缘字符,开始删除
    while i<len(list_to_s):
        if list_to_s[i]==1:
            del list_to_s[i]
            temp_list=list(s)
            del temp_list[i]
            s=''.join(temp_list)
            i=0
            continue
        i+=1

    s_now=s

    if s_last==s_now:
        break

if s=="":
    print("EMPTY")
else:print(s)