# 定义类的语法:class 类名
class Washer():
    def __init__(self,m,n):
        self.height = m
        self.weight = n

    # 定义方法
    def wash(self):
        print('我会洗衣服')

    def pri_info(self):
        print(f'11{self.weight}')
        print(f'22{self.height}')
    def __str__(self):
        return f'长度是{self.weight},宽度是{self.height}'

# 实例化
haier1 = Washer(60,59)
# haier1.wash()
# print(f'阿斯蒂芬{haier1.height}')
# print(f'asdf{haier1.weight}')

haier1.pri_info()

 

print(haier1)