#练习1：定义一个类描述数字时钟
from time import sleep # 导入time模块中的sleep函数
class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour # 小时，
        self.minute = minute # 分钟，
        self.second = second # 秒
    def run(self): # 赋予Clock运动属性，走字。
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self): # 显示时间
         return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)

def main():
    clock = Clock(23, 59, 59)
    while True:
        print(clock.show()) # 调用Clock类中的show方法，这里要先创建一个Clock类得实例clock，
        # 然后再通过clock.show()调用show方法，才能显示时间,而不是直接用Clock.show()。
        clock.run()
        sleep(1) # 每秒走一次

if __name__ == '__main__':
    main()