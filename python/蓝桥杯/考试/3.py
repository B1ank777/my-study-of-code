l1=input().split(" ")
bottle=input().split(" ")
n=int(l1[0])
k=int(l1[1])

for i in range(len(bottle)):
    bottle[i]=int(bottle[i])

color=[]

for i in range(k):
    color.append(i)

average=[]
for i in range(k):
    index=i
    sum=0
    cnt=0
    while index<n:
        sum+=bottle[index]
        cnt+=1
        index+=k
    average.append(sum//cnt)

min=average[0]
for i in range(k):
    if average[i]<min:
        min=average[i]
print(min)