import math
from itertools import combinations

def compute_gcd(a, b, c):
    g = math.gcd(abs(a), abs(b))
    g = math.gcd(g, abs(c))
    return g

points = [(x, y) for x in range(20) for y in range(21)]
lines = set()

for p1, p2 in combinations(points, 2):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 and y1 == y2:
        continue  # 跳过相同的点

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    g = compute_gcd(A, B, C)

    if g != 0:
        A //= g
        B //= g
        C //= g

    # 调整符号，确保A和B的标准化形式
    if A < 0 or (A == 0 and B < 0):
        A = -A
        B = -B
        C = -C

    lines.add((A, B, C))

print(len(lines))