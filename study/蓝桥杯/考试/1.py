from operator import index

get_hw=[]
get_hw=input().split(" ")
h=int(get_hw[0])
w=int(get_hw[1])

num_2025=[2,0,2,5]
G=[[] for _ in range(h)]
index=-1

def get_index(x):
    """
    得到索引值
    :param x: 之前的索引
    :return: 改变之后的索引
    """
    x=x+1
    if x <=3:
        return x
    elif x >3:
        return 0

# 设置第一行
for i in range(w):
    index=get_index(index)
    G[0].append(num_2025[index])

# 开始其他行
for i in range(1,h):
    current=[]
    current=G[i-1].copy()
    del current[0]
    index=get_index(index)
    current.append(num_2025[index])
    G[i]=current.copy()

# 输出
for i in range(h):
    for j in range(w):
        G[i][j]=str(G[i][j])
    s=''.join(G[i])
    print(s)