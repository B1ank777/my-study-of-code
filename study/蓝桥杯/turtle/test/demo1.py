import turtle as t

# 绘制大风车

# 设置画布,画笔
t.setup(500,500)
t.pd()
t.pencolor('green')
t.pensize(10)

# 每一篇扇叶,定义函数
def leaf():
    t.left(45)
    t.fd(150)
    t.left(90)
    t.circle(150,45)
    t.left(90)
    t.fd(150)
    t.right(180)

# 循环4次
for i in range(4):
    leaf()

t.down()