# 定义类的语法:class 类名
class Washer:
    # 定义方法
    def wash(self):
        print('我会洗衣服')

    #在类内部调用属性
    def pri_info(self):
        print(f'{self.height}')
        print(f'{self.weight}')
# 实例化
haier1 = Washer()

# 在类外部添加属性
haier1.height = 800
haier1.meight = 600

# 调用实例方法

haier1.wash()
