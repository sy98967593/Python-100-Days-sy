from random import randint


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))



def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c
print(add()) # 这里的add()并没有指定参数，所以使用默认值
print(add(1)) # 这里的add(1)是指定第几个参数？ 所以只给a传参
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))