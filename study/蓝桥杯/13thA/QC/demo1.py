import math

# 判断是否是质数
def is_prime(x):
    if x<2:
        return False
    else:
        for i in range(2,math.isqrt(x)+1):
            if x%i==0:
                return False
    return True

# 生成一个2到n的质数表
def create_primelist(n):
    p=[]
    for i in range(2,n+1):
        if is_prime(i):
            p.append(i)
    return p

n=int(input("请输入一个数"))

z=create_primelist(n)
cnt=0
for i in z:
    if(n%i==0):
        print(i)
        cnt +=1
print(cnt)