# 定义一个父类
class Teacher(object):
    # 初始化方法
    def __init__(self):
        self.kongfu = '[葵花宝典]'

    # 定义一个称霸武林的方法
    def PK1(self):
        print(f'运用{self.kongfu}称霸武林')


# 定义一个学校类
class School():
    # 初始化方法
    def __init__(self):
        self.kongfu = '[降龙十八掌]'

    # 定义一个称霸武林的方法
    def PK1(self):
        print(f'运用{self.kongfu}称霸武林')


# 定义一个学生类,继承父类
class Student(School,Teacher):
    pass


if __name__ == '__main__':
    # 实例化学生对象
    stu1 = Student()
    # 调用实例属性
    print(stu1.kongfu)
    # 调用实例方法
    stu1.PK1()
