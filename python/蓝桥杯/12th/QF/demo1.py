# 题干给出到毫秒级
from numpy.core.defchararray import zfill

x = int(input("请输入时间:"))
# 得到秒
s = x // 1000
m = s // 60
h = m // 60
# 计算有多少整天,然后再减去,这里直接取余
h = h % 24
m = m % 60
s = s % 60

print(f"{h:02d}:{m:02d}:{s:02d}")