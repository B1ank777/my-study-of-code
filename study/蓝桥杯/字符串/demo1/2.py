count = 0
for i in range(1,2020):
    str1 = str(i)
    if str1.count('9') > 0:
        count = count + 1
print(count)