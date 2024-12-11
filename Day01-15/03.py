# 用户身份验证
username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')


"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""
x = float(input('请输入x的值：'))
if x > 1:
    y = 3 * x - 5
elif x >= -1: # 注意：这里不是else if ，而是elif
    y = x + 2
else: # x < -1
    y = 5 * x + 3
print('f(%.1f) = %.1f' % (x, y))

