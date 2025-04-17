import turtle as t
from operator import index

# 绘制彩色同心圆
# 设置画布,画笔的粗细
t.setup(500,500)
t.pensize(1)
# 颜色,采用list
colors = ['red','green','blue']
# 函数 绘制圆,在此处设置画笔的颜色
def circle(index,r):
    t.pencolor(colors[index])

    # 从圆心出发,走一个半径,开始画圆,然后回到圆心
    t.pu()
    t.fd(r)
    t.left(90)
    t.pd()
    t.circle(r,360)
    t.pu()
    t.home()
# 循环
i = 0
for r in [20,50,100]:
    circle(i,r)
    i+=1