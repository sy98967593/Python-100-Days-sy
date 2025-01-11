# 1) 计算1~100求和的结果
from multiprocessing.connection import answer_challenge

sum = 0
for x in range(1, 101):
    sum += x
print('1~100求和的结果为：', sum)

# 2) 1~100之间的偶数求和
sum = 0
for x in range(100, 0, -2): # 或者 for x in range(2, 101, 2):
    sum += x
print('1~100之间的偶数求和为：', sum) # 结果是 2550

# 3)计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），
# 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续
import random
answer = random.randint(1, 100)
counter = 0
while True:
    guess = int(input('请输入一个1~100之间的数字：'))
    counter += 1
    if guess > answer:
        print('Too Big')
    elif guess < answer:
        print('Too small')
    else:
        print('You got it!')
        break
print('You guessed', counter, 'times')
if counter > 7:
    print('You little loser')


# 4) 输出一个九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (i, j, i*j), end='\t') # end='\t'表示不换行
    print() # 换行


# 5) 练习1：输入一个正整数判断是不是素数, 提示：素数指的是只能被1和自身整除的大于1的整数
import math
x = int(input('请输入一个正整数：'))
x_sqrt = int(math.sqrt(x))
if x > 1:
    for i in range(2, x_sqrt+1):
        if x % i == 0:
            print(x, '不是素数')
            break
        else:
            print(x, '是素数')

