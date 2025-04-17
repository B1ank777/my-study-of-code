N = 15
i = 1
count = 0

for i in range(1,N+1):
    if N % i == 0:
        count = count + 1
        print(i)

print(count)
