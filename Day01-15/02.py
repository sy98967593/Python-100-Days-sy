# 练习1：华氏温度转换摄氏温度
F = float(input('请输入华氏温度：'))
C = (F-32)/1.8
print('%.2f华氏度 = %.2f摄氏度' % (F, C))

# 练习2：输入圆的半径计算计算周长和面积。
import math
r = float(input('圆的半径：'))
print('半径为%.2f的圆周长为%.2f' % (r, 2*math.pi*r))

# 练习3：输入年份判断是不是闰年。
year = int(input('年份：'))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print('%d年是闰年' % year)
else:
    print('%d年不是闰年' % year)

# 练习4：输入一个整数，判断是几位数。
num = int(input('整数：'))
count = len(str(num))
print('%d是%d位数' % (num, count))

