"""4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量"""

"""
定义类
士兵类
属性
姓名 外界 字符串
武器 外界 gun的实例
方法
开火:扣动扳机
装填子弹 给枪加子弹

枪类
属性
枪名 外界 字符串
子弹数量 外界 整数默认30
方法
装弹 子弹数量+=5
射击 判断子弹数是否大于0 
    大于1 哒哒哒,子弹数量-=1
    小于1 提示"你在逗我吗"
str方法
"""


# 枪类
class Gun():
    # 属性
    def __init__(self, gunname, gunnum=30):
        # 枪名 外界 字符串
        self.gunname = gunname
        # 子弹数量 外界 整数默认30
        self.gunnum = gunnum

    # 方法
    def zhuangdan(self):
        # 装弹 子弹数量+=1
        if self.gunnum + 15 < 30:
            self.gunnum += 15
        else:
            print('弹夹就30发,你想干啥?')

    # 射击
    def shoot(self):
        # 判断子弹数是否大于0
        if self.gunnum - 5 > 0:
            #     大于1 哒哒哒,子弹数量-=5
            print('哒哒哒')
            self.gunnum -= 5
        #     小于1 提示"你在逗我吗"
        else:
            print('你在逗我吗?子弹不够啊兄弟')

    # str方法
    def __str__(self):
        return f'我这是{self.gunname},还剩{self.gunnum}发子弹'


# 士兵类
class soldier():
    # 属性
    def __init__(self, name, weapon):
        # 姓名 外界 字符串
        self.name = name
        # 武器 外界 gun的实例
        self.weapon = weapon

    # 方法
    # 开火:扣动扳机
    def fire(self):
        self.weapon.shoot()

    # 装填子弹 给枪加子弹
    def soldierjia(self):
        self.weapon.zhuangdan()

    # str
    def __str__(self):
        return f'大兵名叫{self.name},手持武器{self.weapon}'


if __name__ == '__main__':
    ak47 = Gun('ak47', 25)
    print(ak47)
    ak47.zhuangdan()
    print(ak47)
    ak47.shoot()
    print(ak47)
    Rain = soldier('rain', ak47)
    print(Rain)
    Rain.fire()
    print(Rain)
