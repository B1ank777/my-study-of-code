import math
from collections import defaultdict

n = 2021

# 构建邻接表
adj = [[] for _ in range(1,n+1)]
for i in range (1,n+2):
    for j in range(1,n+2):
        # 计算权重
        if i == j:
            continue

        g = math.gcd(i,j)
        lcm = i * j // g
        adj[i].append((j,lcm))

# 建立一个字典,key为位掩码,用来反映有哪些点已经被遍历到,value为遍历这些点的路径数
current = defaultdict(int)
initial_mask = 1 << 0
current[(initial_mask,0)] = 1

# 从0开始遍历
for _ in range(n-1):
    next_dp = defaultdict(int)
    for (mask,u),cnt in current.items():
        for v in adj[u]:
            if not (mask & (1 << v)):
                new_mask = mask | (1 << v)
                next_dp[(new_mask, v)] += cnt
    current = next_dp

full_mask = (1 << n_nodes) - 1
total = sum(cnt for (mask, u), cnt in current.items() if mask == full_mask)
print(total)
print(adj)