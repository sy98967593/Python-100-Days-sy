#寻找水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10 # //是整数除法, // 10表示取整数部分, % 10表示取余数部分
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

#将12345变成54321
num = int(input('请输入数字：')) # input()函数返回的是字符串类型，需要用int()函数将其转化为整数类型，
print(str(num)[::-1]) # [::-1]表示从后往前取，步长为-1

