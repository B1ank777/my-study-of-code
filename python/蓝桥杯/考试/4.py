n=int(input())
num_list=input().split(" ")

num_of_6=[]

for i in range(n):
    num_of_6.append(num_list[i].count('6'))


for i in range(n):
    for j in range(n-1):
        if num_of_6[j]<num_of_6[j+1]:
            temp=num_of_6[j]
            num_of_6[j]=num_of_6[j+1]
            num_of_6[j+1]=temp

left=0
right=n-1
cnt=0

while left<right:
    if num_of_6[left]>=6:
        left+=1
        cnt+=1
        continue

    if num_of_6[left]+num_of_6[right]>=6:
        left+=1
        right-=1
        cnt+=1
        continue

    if num_of_6[left]+num_of_6[right]+num_of_6[right-1]>=6:
        left+=1
        right-=2
        cnt+=1
        continue

    if num_of_6[left]+num_of_6[right]+num_of_6[left+1]>=6:
        left+=2
        right-=1
        cnt+=1
        continue
    else:
        break
print(cnt)