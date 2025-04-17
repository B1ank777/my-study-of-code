import math
from itertools import combinations
# 计算3个数最大公约数的函数
def three_gcd(a,b,c):
    g = math.gcd(abs(a),abs(b))
    g = math.gcd(g,abs(c))
    return g

# 得到每个点对,放在一个列表中
points = [(x,y)for x in range(20) for y in range(21)]
# 创建一个集合放直线,格式为(A,B,C)
lines = set()

# 使用combination函数,取每两个坐标,x1,y1,x2,y2
for p1,p2 in combinations(points,2):
    x1,y1 = p1
    x2,y2 = p2

# 计算这个点对的直线方程形式为Ax+By+C=0
# A = y2-y1,B = x2-x1,C = x2*y1-x1*y2
    A = y2-y1
    B = x2-x1
    C = x2*y1-x1*y2

# 得到3个点的最大公约数,化简,放入一个集合中
    g = three_gcd(A,B,C)
    if g != 0:
        A //= g
        B //= g
        C //= g

    lines.add((A,B,C))
# 输出集合的大小
print(len(lines))