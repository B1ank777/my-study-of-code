data = [2,1,3,5,4]
count = 0

for i in range(0,len(data)):
    s = data[i]
    b = data[i]

    j = 0
    for j in range(0,len(data)):
        if data[j] < s:
            s = data[j]
        if data[j] > b:
            b = data[j]


    if s != data[i] and b != data[i]:
        count = count + 1

print(count)