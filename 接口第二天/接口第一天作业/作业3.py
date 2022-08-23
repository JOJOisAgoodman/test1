"""
3、摆放家具
    需求：
    1）.房子有户型，总面积和家具名称列表
       新房子没有任何的家具
    2）.家具有名字和占地面积，其中
       床：占4平米
       衣柜：占2平面
       餐桌：占1.5平米
    3）.将以上三件家具添加到房子中
    4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

"""

"""
定义类:
房子
属性
户型 外界 字符串
面积 外界 数值
剩余面积 外界 数值
家具列表 空 列表
方法
摆放家具
if 家具面积小于剩余面积 可以摆进房子 剩余面积-=家具面积
否则 提示报错
家具
属性
名称 外界 字符串
家具面积 外界 数值


"""


# 定义类:
# 房子
class House():
    # 属性
    def __init__(self, huxing, zongmianji):
        # 户型 外界 字符串
        self.huxing = huxing
        # 面积 外界 数值
        self.zongmianji = zongmianji
        # 剩余面积 外界 数值
        self.shengmianji = zongmianji
        # 家具列表 空 列表
        self.jiajulist = []

    # 方法
    def baifang(self, jiaju):
        # 摆放家具
        # if 家具面积小于剩余面积 可以摆进房子 剩余面积-=家具面积
        # 否则 提示报错
        if jiaju.jiajumianji < self.shengmianji:
            self.jiajulist.append(jiaju.jiajuname)
            self.shengmianji -= jiaju.jiajumianji
        else:
            print('地方不够用了啊.换个别的吧')
            return

    def __str__(self):
        return f'房子的户型是{self.huxing},房子面积总共{self.zongmianji},剩余面积{self.shengmianji},摆放家具有{self.jiajulist}'


# 家具
class Jiaju():
    # 属性
    # 名称 外界 字符串
    def __init__(self, jiajuname, jiajumianji):
        self.jiajuname = jiajuname
        # 家具面积 外界 数值
        self.jiajumianji = jiajumianji

    def __str__(self):
        return f'家具名字是{self.jiajuname},占用{self.jiajumianji}'


if __name__ == '__main__':
    zhuozi = Jiaju('桌子', 1.5)
    chuang = Jiaju('床', 25)
    print(zhuozi)
    dasanju = House('大三居', 20)
    print(dasanju)
    dasanju.baifang(zhuozi)
    print(dasanju)
    dasanju.baifang(chuang)
    print(dasanju)
