import itertools
from itertools import repeat


def can_form_large_rect(a,b):
    """
    检查这三个具体尺寸的矩形能否拼成一个更大的矩形
    :param a:三个矩形的宽度
    :param b:三个矩形的高度
    :return:True/False
    """
    # 如果能拼成一个大矩形,计算这个矩形的面积
    sum_area=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    if sum_area==0:
        return True

    factors=[] #存放可能最大矩形的宽和高

    for A in range(1,int((sum_area**0.5)+1)):
        if sum_area%A==0:
            factors.append((A,sum_area//A))
            if A!=sum_area//A:
                factors.append((sum_area//A,A))

    # 遍历所有的可能的大矩形,判断能否用小矩形拼出来
    for A,B in factors:
        # 情况1,三个矩形横向拼接
        if b[0]==b[1]==b[2] and (a[0]+a[1]+a[2]==A):return True

        # 情况2,两个矩形横向并排,第三个在上方或下方
        for i in range(3):
            for j in range(3):
                if i==j:continue
                k=3-i-j
                if a[i]+a[j]==A and b[i]==b[j]:
                    h=b[i]
                    if b[k]==B-h and a[k]==A:return True

        # 情况3,三个矩形纵向拼接
        if a[0]==a[1]==a[2] and (b[0]+b[1]+b[2]==B):return True

        # 情况4,两个矩形纵向堆叠,第三个在左或者右
        for i in range(3):
            for j in range(3):
                if i==j:continue
                k=3-i-j
                if b[i]+b[j]==B and a[i]==a[j]:
                    w=a[i]
                    if a[k]==A-w and b[k]==B:return True

        return False

def minimal_sides(rectangles):
    """
    找出是否存在一种旋转组合,能拼成一个大矩形,可以则返回4,不行则返回6
    :param rectangles:包含三个矩形的列表
    :return:4/6
    """
    min_sides=6

    for dirs in itertools.product([0,1],repeat=3):# 生成所有长度为3,由0,1组成的元组
        # 0表示矩形的原始状态,1表示矩形旋转90度
        a,b=[],[]

        for i in range(3):
            if dirs[i]==0:
                ai,bi=rectangles[i][0],rectangles[i][1]
            else:
                ai,bi=rectangles[i][1],rectangles[i][0]
            a.append(ai)
            b.append(bi)

        if can_form_large_rect(a,b):return 4

        return min_sides

rects=[]
T=input()
a1,b1,a2,b2,a3,b3=map(int,input().split(" "))
rects.append((a1,b1))
rects.append((a2,b2))
rects.append((a3,b3))

print(minimal_sides(rects))