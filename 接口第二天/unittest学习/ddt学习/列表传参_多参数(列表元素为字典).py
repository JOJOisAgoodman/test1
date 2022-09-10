import unittest
from ddt import ddt,unpack,data

list1 = [{"value1":1,"value2":2},{"value1":2,"value2":2}]
@ddt
class myTest1(unittest.TestCase):
    # @data({"value1":1,"value2":2},{"value1":2,"value2":2})
    # @unpack
    # def test_b1(self,value1,value2):
    #     print(f"第一个数是{value1},第二个数是{value2}")
    #     self.assertEqual(value1,value2,"两个数不相等")
    @data(*list1)
    @unpack
    def test_b1(self, value1, value2):
        print(f"第一个数是{value1},第二个数是{value2}")
        self.assertEqual(value1, value2, "两个数不相等")

if __name__ == '__main__':
    unittest.main(verbosity=2)