import heapq
# 通过取负数模拟最大堆
max_heap = []
nums = [3, 1, 4, 1, 5]
for num in nums:
    heapq.heappush(max_heap, -num)
print(heapq.heappop(max_heap))
print(-heapq.heappop(max_heap))  # 输出 5（最大值）