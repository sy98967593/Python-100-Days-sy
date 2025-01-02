'''使用相对路径'''
import os
f1=os.getcwd()
print(f1) #获取当前工作目录，将需要打开的TXT文件放入刚才找到的同一个文件夹

def main(): # 定义一个函数

    f = open('致橡树.txt', 'r', encoding='utf-8') # r表示只读， encoding='utf-8'表示编码格式为utf-8
    print(f.read()) # read()表示读取文件的全部内容
    f.close() # close()表示关闭文件

if __name__ == '__main__':
    main()

'''使用绝对路径'''
def main(): # 定义一个函数

    f = open(
        'D:\\Yan Shi Data\【1】先进技术部\【3】研发项目\大数据智能化\python学习\Python-100-Days-sy\Day01-15\登鹳雀楼.txt',
        'r', encoding='utf-8') #绝对路径要输入文件的完整地址，
    print(f.read()) # read()表示读取文件的全部内容
    f.close() # close()表示关闭文件

if __name__ == '__main__':
    main()


'''使用try-except语句处理文件不存在、编码错误等异常情况'''
def main():
    f = None # 定义一个变量f，初始值为None
    try: # try语句块，用于尝试执行可能会出现异常的代码
        f = open('登鹳雀楼.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError: # except语句块，用于处理try语句块中出现的异常
        print('无法打开指定的文件!')
    except LookupError: # LookupError是UnicodeDecodeError的父类，用于处理编码错误
        print('指定了未知的编码!')
    except UnicodeDecodeError: # UnicodeDecodeError是LookupError的子类，用于处理解码错误
        print('读取文件时解码错误!')
    finally: # finally语句块，无论是否出现异常，都会执行
        if f: # 判断f是否为None，如果不是None，则执行close()方法关闭文件
            f.close() # close()方法用于关闭文件

if __name__ == '__main__':
    main()


'''用for-in方法读取和用readline方法读取'''
import time

def main():
    #一次性读取整个文件
    with open('登鹳雀楼.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    #一行一行地读取文件
    with open('登鹳雀楼.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='') # end=''表示不换行
            time.sleep(1) # 暂停0.5秒
    print()
    f.close()
    #读取文件按行读取到列表中
    with open('登鹳雀楼.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines) # 打印列表，注意这里是列表
    f.close()
if __name__ == '__main__':
    main()


'''将1-9999之间的素数分别写入三个文件中
（1-99之间的素数保存在a.txt中，
100-999之间的素数保存在b.txt中，
1000-9999之间的素数保存在c.txt中）'''
def main():
    f1 = open('a.txt', 'w', encoding='utf-8')
    f2 = open('b.txt', 'w', encoding='utf-8')
    f3 = open('c.txt', 'w', encoding='utf-8')
    for num in range(1, 10000):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                if num < 100:
                    f1.write(str(num) + ' ')
                elif 100 <= num < 1000:
                    f2.write(str(num) + ' ')
                else:
                    f3.write(str(num) + ' ')
    f1.close()
    f2.close()
    f3.close()
if __name__ == '__main__':
    main()



