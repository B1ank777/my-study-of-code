# 得到杨辉三角,由嵌套的队列组成
import sys

yanghui = [[] for _ in range(1000)]
# 初始化第一行和第二行
yanghui[0] = [1]
yanghui[1] = [1,1]
# 往后每一行的数,第一个是1,后面由上一个得到,直到将上一个最后一个遍历到,再补上1
for i in range(2,1000):
    yanghui[i].append(1)

    for j in range(1,len(yanghui[i-1])):
        yanghui[i].append(yanghui[i-1][j-1]+yanghui[i-1][j])


    yanghui[i].append(1)

# 已经得到杨辉三角
x = int(input("请输入您的数字:"))
cnt = 0
for i in range(1000):
    for j in range(len(yanghui[i])):
        if x == yanghui[i][j]:
            print(cnt + 1)
            sys.exit()
        else:
            cnt += 1
