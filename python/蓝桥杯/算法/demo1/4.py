import heapq
num_list=input().split(" ")
target=int(input())
len1=len(num_list)
for i in range(len1):
    num_list[i]=int(num_list[i])
    if num_list[i]>target:
        num_list[i]=-1

less_heap=[]
more_heap=[]
eq=[]
for i in range(len1):
    if (target // 2) > num_list[i] > 0:
        heapq.heappush(less_heap,(num_list[i],i))
    if num_list[i]>target//2:
        heapq.heappush(more_heap,(-num_list[i],i))
    if num_list[i]==target//2:
        eq.append((num_list[i],i))

if len(eq)==2:
    print(f"{eq[0][1]},{eq[1][1]}")

while less_heap and more_heap:
    less,index_of_min = heapq.heappop(less_heap)
    more,index_of_max = heapq.heappop(more_heap)

    if less+(-more)>target:
        heapq.heappush(less_heap,(less,index_of_min))
    elif less+(-more)<target:
        heapq.heappush(more_heap,(-more,index_of_max))
    else:
        print(f"{(less,index_of_min)},{-more,index_of_max}")
        