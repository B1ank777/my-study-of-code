def rank(listA):
    """
    将listA从小到大排序
    :param listA: 输入的那一串整数
    :return:重新排序后的数组
    """
    temp_list=listA
    min=temp_list[0]
    after_rank_listA=[]
    index=0

    for _ in range(len(listA)):
        for j in range(len(temp_list)):
            if temp_list[j]<min:
                min=temp_list[j]
                index=j

        del temp_list[index]
        after_rank_listA.append(min)

    return after_rank_listA

print(rank([2,3,4,1,5]))