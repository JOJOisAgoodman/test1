import unittest
from ddt import ddt, data, unpack

# 测试数据
list1 = [[1,2],[2,2],[3,2]]
@ddt
class myTest1(unittest.TestCase):
    # # 单个传参
    @data(*list1)
    @unpack
    def test_bb1(self,value1,value2):
        print(f'第一个数是{value1},第二个数是{value2}')
        # self.assertEqual(value1, value2, f'第一个数{value1}和第二个数{value2},两个数不相等')
        try:
            self.assertEqual(value1, value2, f'第一个数{value1}和第二个数{value2},两个数不相等')
        except Exception as result:
            print(result)
            raise
        else:
            return

    # @data(*list1)
    # @unpack
    # def test_bb1(self, value1, value2):
    #     print(f'第一个数是{value1},第二个数是{value2}')
    #     self.assertEqual(value1, value2, f'第一个数{value1}和第二个数{value2},两个数不相等')


if __name__ == '__main__':
    unittest.main(verbosity=2)