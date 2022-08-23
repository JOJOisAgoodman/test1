# 定义一个父类
class A():
    def __init__(self):
        self.num = 1
    def printi(self):
        print(self.num)
class B(A):
    pass

if __name__ == '__main__':
    b = B()
    res = b
    print(res)
    res.printi()