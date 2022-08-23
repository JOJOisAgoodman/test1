# 定义一个父类
class Teacher(object):
    # 初始化方法
    def __init__(self):
        self.kongfu = '[葵花宝典]'
        self.__kongfu = '[七伤拳]'

    # 定义一个称霸武林的方法
    def PK1(self):
        print(f'运用{self.kongfu}称霸武林')

    def __get_kongfu(self):
        print(self.__kongfu)

    def set_kongfu(self, cnkongfu):
        if cnkongfu == True:
            print(self.__kongfu)
        else:
            print('666')


# 定义一个学生类,继承父类
class Student(Teacher):
    pass


if __name__ == '__main__':
    # 实例化学生对象
    stu1 = Student()
    # 调用实例属性
    stu1.set_kongfu(1)
    # 调用实例方法
    stu1.PK1()
    print(stu1)
