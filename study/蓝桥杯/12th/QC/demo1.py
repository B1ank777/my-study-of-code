# 对2021041820210418分解质因数,并记录每个质因数的个数,用字典存储起来
# 从开始,将2021041820210418中所有的2除尽,然后是3...
from symbol import factor
import math
n = 2021041820210418

fac = {}

# 分解2
i = 2
while n % 2 == 0:
    fac[2] = fac.get(2,0) + 1
    n //= 2

# 分解3
i = 3
while n % 3 == 0:
    fac[3] = fac.get(3,0) + 1
    n //= 3

# 分解5以上
i = 5
# 计算n的平方根,在小于n的平方根中找质数,找到后,就将n整除了,再计算新数的平方根
# 计算可能出现的最大的质数,即平方根
max_factor = math.isqrt(n)+1
while i <= max_factor and n > 1:
    while n % i == 0:
        fac[i] = fac.get(i,0) + 1
        n //= i
        max_factor = math.isqrt(n)+1
    i += 2

x = 2021041820210418
for i in fac.keys():
    # print(i)
    for j in range(fac[i]):
        x //= i

fac[x] = fac.get(x,0) + 1
# print(x)
# print(fac)
# print(len(fac))
# print(fac.keys())
