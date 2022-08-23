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
class Student(School, Teacher):
    def __init__(self):
        super().__init__()
        self.kongfu1 = '[九阴白骨爪]'

    def PK2(self):
        print(f'运用{self.kongfu1}称霸武林')
    #定义一个老师类的方法
    def PK3(self):
        Teacher.__init__(self)
        Teacher.PK1(self)

    # 定义一个功夫方法,调用父类不同方式
    def PK1_1(self):
        # 方法一:指名道姓    优点:可以灵活调用某个父类的属性和方法
        #缺点:父类改名,需要频繁修改类名
        # School.__init__(self)
        # School.PK1(self)
        #方法二:super调用父类方法
        # super(Student, self).PK1()
        super().__init__()

if __name__ == '__main__':
    # 实例化学生对象
    stu1 = Student()
    # 调用实例属性
    # print(stu1.kongfu1)
    # # 调用实例方法
    # stu1.PK1()
    # stu1.PK3()
    # stu1.PK2()
    stu1.PK1_1()