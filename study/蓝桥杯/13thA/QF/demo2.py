n=input()
listA=input().split(" ")
m=int(input())
all_LR=[]
for _ in range(m):
    all_LR.append(input().split(" "))

for i in range(len(listA)):
    listA[i]=int(listA[i])

# def sum(all_LR,listA):
#     """
#     计算原本的sum
#     :param LR: 查询的路径
#     :return: sum
#     """
#     sum=0
#     for i in range(m):
#         for j in range(int(all_LR[i][0])-1,int(all_LR[i][1])):
#             sum += listA[j]
#     return sum

# print(sum(all_LR,listA))

def num_of_closed(all_LR,listA):
    """
    通过LR计算出每个位置被覆盖的次数
    :param LR: 查询的路径
    :return: 列表,对应次数
    """
    closed=[]
    for _ in range(len(listA)):
        closed.append(0)
    for i in range(m):
        for j in range(int(all_LR[i][0])-1,int(all_LR[i][1])):
            closed[j] += 1

    return closed
print(num_of_closed(all_LR,listA))


print(listA)