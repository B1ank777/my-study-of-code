from itertools import permutations

# 输入一个数字用列表存储,并转化为int类型
max_num=int(input())

num_list=[]

for i in range(1,max_num+1):
    num_list.append(i)

# print(num_list)

# def permutation(list):
#     """
#     得到一个列表的全排列
#     :param list: 列表
#     :return: 嵌套列表per[[]]
#     """
#     if len(list)<1:
#         return [list[:]]
#
#     result=[]
#     for i in range(len(list)):
#         current=list[i]
#         remain=list[:i]+list[i+1:]
#         for p in permutation(remain):
#             result.append([current]+p)
#
#     return result


def sum(perm):
    """
    由全排列的列表计算value
    :param perm: perm
    :return: sum_of_value
    """
    sum_of_value=0
    for i in range(len(perm)):
        value=0
        for j in range(len(perm[i])):
            a=perm[i][j]
            c=0
            for k in range(0,j):
                if a<perm[i][k]:
                    c+=1
            value+=c
        sum_of_value+=value

    return sum_of_value

perm=list(permutations(num_list))
print(sum(perm)%998244353)