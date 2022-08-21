"""
定义类:地瓜
状态 status str 默认:生的
被烤的时间 time1 int 默认0
方法:cook方法
时间 time 外界给与
烤的时间 +=time
判断
if else
"""


class digua():
    def __init__(self):
        self.status = '生的'
        self.time1 = 0
        self.list1 = []

    def cook(self, time):
        self.time1 += time
        if 0 < self.time1 <= 3:
            self.status = '生的'

        elif 3 < self.time1 <= 5:
            self.status = '半生不熟'

        elif 5 < self.time1 <= 8:
            self.status = '熟了'


        elif self.time1 > 8:
            self.status = '糊了'


        else:
            print('输入错误重新输入')

    def tiaoliao(self,tiaoliao):
        self.list1.append(tiaoliao)

    def shuru(self):
        self.cook(int(input('你想考多久')))
        self.tiaoliao(input('你要放什么调料'))
        print(p1)

    # def tiaoliao(self,*args):
    #     self.list1.extend(args)

    def __str__(self):
        return f"烤了{self.time1},是{self.status},调料放了{self.list1}"

if __name__ == '__main__':
    p1 = digua()

    while True:
        p1.shuru()
        if p1.status == "熟了" or p1.status == "糊了":
            print('赶紧吃吧,都熟了')
            break
        else:
            print('没熟啊')



