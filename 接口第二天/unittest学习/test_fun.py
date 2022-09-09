from myfun import *
import unittest

"""
测试用例:
1.测试用例的类续继承unittest.TestCase类
2.测试方法需要用test开头
"""


# 定义一个测试类
class Mytest(unittest.TestCase):
    def setUp(self) -> None:
        print('准备工作!!')

    def tearDown(self) -> None:
        print('清理工作')

    @classmethod#类
    def setUpClass(cls) -> None:
        print('所有用例的准备工作!!!!')

    @classmethod
    def tearDownClass(cls) -> None:
        print('所有用例的清理工作')

    # 定义测试方法
    def test_add(self):
        print('----->执行')
        real = add(1, 2)

        # 断言
        self.assertEqual(real, 3, '与预期结果不一致')


    # @unittest.skip('直接跳过')
    # @unittest.skipIf(True,'是真就跳过')
    # @unittest.skipUnless(False,"是假就跳过")
    def test_mul(self):
        print("----->执行!")
        real = minus(2, 3)
        if real<0:
            self.skipTest('小于零跳过这条用例')#用于条件后跳过..
        self.assertEqual(real, 0, '与预期结果不一致')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    # 创建一个空的测试用例套件
    suite = unittest.TestSuite()
    # 调用实例化方法添加测试用例到套件内
    # suite.addTest(Mytest('test_add'))
    # suite.addTest(Mytest('test_mul'))
    suite.addTests([Mytest('test_add'),Mytest('test_mul')])
    # 实例化一个执行对象
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)