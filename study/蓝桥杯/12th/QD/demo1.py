# Dijkstra算法计算最短路径
import math
import heapq
n = 2021
# 先生成一个邻接表
adj = [[] for _ in range(0,n+1)]
# adj[u]= (v,w) 表示u到v的距离为w
for i in range(1,n+1):
    for j in range(i+1,min(i+21,n)+1):
        # 计算权重
        g = math.gcd(i,j)
        lcm = i * j // g
        adj[i].append((j,lcm))
        adj[j].append((i,lcm))

# 构造距离数组
dist = [float('inf')]*(n+1) # index表示1到这个索引的距离
dist[1] = 0

# 采用堆,最小堆的根是最小的,所以弹出顶点就是这些路径中最短的路径
heap = []
heapq.heappush(heap,(0,1))

# 循环堆,直到堆清空
while heap:
    current_dist,u = heapq.heappop(heap)

    if u == n:
        break

    if current_dist > dist[u]:
        continue

    for v,w in adj[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(heap,(dist[v],v))


print(dist[n])
# 弹出current_dist和u,current_dist表示点1到点u的最短的路径长度
# 如果需要弹出的确定最短的路径已经有2021,则结束循环
# 如果弹出的current_dist大于dist[u],则说明已经弹出过了,跳过这个u
