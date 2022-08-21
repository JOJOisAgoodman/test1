# # 方法一:import 模块名
# import my_module
# # 调用：模块名.方法
# my_module.testA(5,3)
#
# # 方法二:from 模块名 import 方法名
# from my_module import testB
# # 调用:方法名
# testB(2,4)
# *代表调用包的全部方法
# from my_module import *
# testA(2,7)
# testB(1,1)

# # 方法三:给模块起别名
# import my_module as my
# # 调用:别名.方法名(),起了名原来的名就不能用了
# my.testA(2,3)
#
# # 方法四:给方法起别名
# from my_module import testB as jia
# jia(2,3)

# from my_module1 import *
# testA(1,2)
# testB(2,3)


# 导包:
# # 方法一:import 包名.模块名
#
# import my_package.my_module
#
# # 调用:包名.模块名.方法名()
# my_package.my_module.info_print1()

# # 方法二:from 包名 import 模块名
# from my_package import my_module1
# # 调用:模块名.方法名()
# my_module1.info_print2()

# # 方法三:from 包名.模块名 import 方法名()
# from my_package.my_module1 import info_print2
# # 调用:方法名()
# info_print2()

from my_package import *
my_module1.info_print2()