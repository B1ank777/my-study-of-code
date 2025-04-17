list1 = [3,2,4,6,7]

for i in range(0,len(list1)):
    j = 0
    for j in range(0,len(list1)-1):
        if list1[j] > list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp

for i in range(0,len(list1)-1):
    if list1[i]+1 != list1[i+1]:
        print(list1[i] + 1)
print(list1)