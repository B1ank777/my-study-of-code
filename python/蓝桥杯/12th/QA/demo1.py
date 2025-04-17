# 设立10个计数器(列表),分别记录0到9的个数
import sys

numcount = [0,0,0,0,0,0,0,0,0,0]
# 第一层循环,从0开始,到100000,
for i in range(10000):
# 对于每一个数字分解,进入第二层循环,比如说123,对应1,2,3的计数器各加1
    numstr = str(i)
    for j in numstr:
        numcount[int(j)] +=1
# 每分解完一个数字就判断计数器是否有大于2021张的,若有,则退出循环
    for k in range(len(numcount)):
        if numcount[k] > 2021:
            print(i-1)
            sys.exit()