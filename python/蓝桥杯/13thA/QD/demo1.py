data_num=input()
a1,b1,a2,b2,a3,b3=input().split(' ')
# m1,n1,m2,n2,m3,n3=input().split(' ')
data1=[]
# data2=[]

data1.append([a1,b1])
data1.append([a2,b2])
data1.append([a3,b3])

# data2.append((m1,n1))
# data2.append((m2,n2))
# data2.append((m3,n3))

for i in range(3):
    data1[i][0]=int(data1[i][0])
    data1[i][1] = int(data1[i][1])
# print(data1[0][0])
def the_others_sum(x,y):
    """
    计算另外两个矩形边的所有组合之和
    :param x: 矩形x
    :param y: 矩形y
    :return: 队列,其中有4个元素
    """
    all_sum=[]
    all_sum.append(x[0]+y[0])
    all_sum.append(x[0] + y[1])
    all_sum.append(x[1] + y[0])
    all_sum.append(x[1] + y[1])
    return all_sum


def sum_equ(data):
    """
    判断是否有两个矩形边之和等于第三个矩形的一条边
    :param data: 存放3个矩形信息的二维数组
    :return: True/False
    """
    for i in range(3):
        if(i-1<0):
            a=i+2
        else:
            a=i-1

        if(i+1>2):
            b=i-2
        else:
            b=i+1

        all_sum=[]
        all_sum=the_others_sum(data[a],data[b])

        for j in all_sum:
            if(j==data[i][0] or j==data[i][1]):
                return True

    return False

def same_age(data):
    """
    检查是否有相同的边,如果有,则将相同的边重合,计算另外两个边之和是否与第三个矩形的边相等
    :param data: 存放3个矩形信息的二维数组
    :return: True/False
    """
    for i in range(3):
        if (i - 1 < 0):
            a = i + 2
        else:
            a = i - 1

        if (i + 1 > 2):
            b = i - 2
        else:
            b = i + 1

        for x in range(2):
            for y in range(2):
                if(data[a][x] == data[b][y]):
                    sum=data[a][x-1]+data[b][y-1]
                    for z in range(2):
                        if(sum==data[i][z]):
                            return True

        return False

if(sum_equ(data1)==True):
    if(same_age(data1)):
        print(4)
    else:
        print(6)
else:print(8)