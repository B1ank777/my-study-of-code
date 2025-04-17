import math


def extended_gcd(a, b):
    """迭代实现的扩展欧几里得算法，返回 (g, x, y) 使得 a*x + b*y = g = gcd(a, b)"""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return (old_r, old_s, old_t)


def merge_one_congruence(n0, mod0, a, r):
    """合并同余式 n ≡ n0 (mod mod0) 和 n ≡ r (mod a)，返回合并后的解"""
    d = math.gcd(mod0, a)
    diff = (r - n0) % a  # 确保diff非负

    if diff % d != 0:
        return (None, None)  # 无解

    # 将方程约简为互质模数形式
    mod0_reduced = mod0 // d
    a_reduced = a // d
    diff_reduced = diff // d

    # 解 mod0_reduced * k ≡ diff_reduced (mod a_reduced)
    g, x, y = extended_gcd(mod0_reduced, a_reduced)
    # 由于约简后gcd(mod0_reduced, a_reduced)=1，解为k ≡ x*diff_reduced mod a_reduced
    k_sol = (x * diff_reduced) % a_reduced

    # 计算合并后的解
    n_new = (n0 + k_sol * mod0) % (mod0 * a_reduced)
    mod_new = mod0 * a_reduced  # LCM(mod0, a)
    return (n_new, mod_new)


def solve_all_congruences(pairs):
    """合并所有同余式，返回最小非负整数解"""
    cur_n, cur_mod = 0, 1  # 初始解为 n ≡ 0 (mod 1)
    for a, r in pairs:
        cur_n, cur_mod = merge_one_congruence(cur_n, cur_mod, a, r)
        if cur_n is None:
            return None
    return cur_n


def main():
    # 构造同余式列表，示例：n ≡ a-1 mod a (a=2到49)
    pairs = [(a, a - 1) for a in range(2, 50)]
    solution = solve_all_congruences(pairs)

    if solution is None:
        print("无解")
    else:
        print(f"最小解 = {solution}")


if __name__ == "__main__":
    main()