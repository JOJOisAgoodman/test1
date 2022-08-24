class Dog():
    # 设置类属性
    tooth = 10

    # 设置实例属性
    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    dahuang = Dog('大黄')
    xiaohei = Dog('小黑')

    # 调用类属性
    print(Dog.tooth)
    print(dahuang.tooth)

    # 调用实例属性
    print(Dog.tooth)
    # print(Dog.name)
    print(dahuang.tooth)
    print(dahuang.name)