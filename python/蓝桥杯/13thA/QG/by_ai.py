MOD = 998244353
inv4 = 748683265  # 4的逆元，计算为pow(4, MOD-2, MOD)

n = int(input())
if n < 2:
    print(0)
else:
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i % MOD
    term = n * (n - 1) % MOD
    product = term * fact % MOD
    ans = product * inv4 % MOD
    print(ans)