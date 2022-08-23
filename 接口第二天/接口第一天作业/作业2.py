"""
2、小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤

"""
"""
定义类:
    人类:
    属性:姓名 外界 字符串
        体重 外界 数值
方法:
    跑步:
    跑步一次,体重-=0.5
    吃:
    吃一次,体重+=1

"""


# 定义类:
class Person():
    #     人类:
    def __init__(self, name, tizhong):
        #     属性:姓名 外界 字符串
        #         体重 外界 数值
        self.name = name
        self.tizhong = tizhong

    # 方法:
    #     跑步:
    def run(self):
        #     跑步一次,体重-=0.5
        self.tizhong -= 0.5

    #     吃:
    def eat(self):
        #     吃一次,体重+=1
        self.tizhong += 1

    def __str__(self):
        return f'我的名字是{self.name},体重是{self.tizhong}公斤'


if __name__ == '__main__':
    xiaoming = Person('xiaoming', 75)
    xiaomei = Person('xiaomei', 45)
    xiaoming.run()
    xiaomei.eat()
    print(xiaomei)
    print(xiaoming)
