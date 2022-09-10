from ddt import ddt, data
import unittest

# 测试数据
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 写一个测试类
@ddt
class myTest(unittest.TestCase):
    # 定义一个测试方法
    # 单个传参
    # @data(2)
    # def test_bb1(self,value):
    #     print('----->执行bb1',value)
    #     self.assertEqual(value,2,'这个不是2')

    # 多个传参
    # @data(2,3,4,5,6,76,8)
    # def test_bb1(self,value):
    #     print('----->执行bb1',value)
    #     self.assertEqual(value,2,'这个不是2')

    # 多个传参(提前定义好的)
    @data(*list1)
    def test_bb1(self, value):
        print('----->执行bb1', value)
        self.assertEqual(value, 2, '这个不是2')


if __name__ == '__main__':
    unittest.main(verbosity=2)
