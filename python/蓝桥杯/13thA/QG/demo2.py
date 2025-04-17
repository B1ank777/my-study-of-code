"""
一共有n!中排列,就意味着i,j一起会出现n!次
而要使i<j,即顺序对(i,j),就要除以2
(i,j)共有Cn2种可能,所以
Cn2*n!/2
"""
MOD=998244353
n=int(input())

if n < 2:
    print(0)
else:
    fact=1
    for i in range(2,n+1):
        fact=fact*i%MOD

    term=n*(n-1)%MOD

    print((term*fact)//4%MOD)
