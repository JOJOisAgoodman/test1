class Dog():
    def work(self):
        print('指哪咬哪')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人')


class DrugDog(Dog):
    def work(self):
        print('抓毒品')


class Person():
    def work_with_dog(self, dog):
        dog.work()


if __name__ == '__main__':
    d1 = Dog()
    d2 = ArmyDog()
    d3 = DrugDog()
    p1 = Person()
    p1.work_with_dog(d3)
