n=input()
listA=input().split(" ")
m=int(input())
all_LR=[]
for _ in range(m):
    all_LR.append(input().split(" "))

for i in range(len(listA)):
    listA[i]=int(listA[i])

# print(data)

def sum(LR,list):
    """
    计算原本的sum
    :param LR: 查询的路径
    :return: sum
    """
    sum=0
    for i in range(m):
        for j in range(int(LR[i][0])-1,int(LR[i][1])):
            sum += list[j]
    return sum

def rank(list):
    """
    将listA从小到大排序
    :param listA: 输入的那一串整数
    :return:重新排序后的数组
    """
    temp_list=list.copy()
    after_rank_listA=[]

    for _ in range(len(list)):
        index = 0
        min = temp_list[0]
        for j in range(len(temp_list)):
            if temp_list[j]<min:
                min=temp_list[j]
                index=j

        del temp_list[index]
        after_rank_listA.append(min)

    return after_rank_listA

def num_of_closed(LR,list):
    """
    通过LR计算出每个位置被覆盖的次数
    :param LR: 查询的路径
    :return: 列表,对应次数
    """
    closed=[]
    for _ in range(len(list)):
        closed.append(0)
    for i in range(m):
        for j in range(int(LR[i][0])-1,int(LR[i][1])):
            closed[j] += 1

    return closed

def get_new_listA(LR,list):
    """
    将listA根据closed重新排序,closed越大,对应index的值越大
    :param LR:
    :param list:
    :return:
    """
    new_listA=[]
    for _ in range(len(list)):
        new_listA.append(0)
    closed=[]
    closed=num_of_closed(LR,list)

    after_rank_listA=rank(list)

    for i in range(len(list)):
        max=closed[0]
        index=0
        for j in range(len(closed)):
            if closed[j]>max:
                max=closed[j]
                index=j

        #注意此处不能删了,否则index就乱了,只能置为0
        closed[index]=-1
        new_listA[index]=after_rank_listA[(len(after_rank_listA)-1)]
        del after_rank_listA[(len(after_rank_listA)-1)]

    return new_listA


o_sum=sum(all_LR,listA)
a_sum=sum(all_LR,get_new_listA(all_LR,listA))
print(get_new_listA(all_LR,listA))
print(a_sum-o_sum)


# print(original_sum(all_LR))