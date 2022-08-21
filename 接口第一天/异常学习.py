# try:
#     open('test.txt','r',encoding='utf-8')
#     print('读打开')
# except:
#     open('test.txt','w',encoding='utf-8')
#     print('写')

# try:
# #     open('test.txt111','r',encoding='utf-8')
# #     print('读打开')
#     print(num)
# except FileNotFoundError:
#     open('test.txt','w',encoding='utf-8')
#     print('写')

# try:
#     open('test.txt111','r',encoding='utf-8')
#     print('读打开')
# except NameError:
#     open('test.txt','w',encoding='utf-8')
#     print('写')

# try:
#     open('test.txt333','r',encoding='utf-8')
#     print('读打开')
#     print(n)
# except (NameError,FileNotFoundError):
#     open('test.txt333','w',encoding='utf-8')
#     print('写,2')

# try:
#     open('test.txt111','r',encoding='utf-8')
#     print('读打开')
# except NameError:
#     open('test.txt222','w',encoding='utf-8')
#     print('写')
# except FileNotFoundError:
#     open('test.txt333', 'w', encoding='utf-8')
#     print('写')


# try:
#     open('test.txt333','r',encoding='utf-8')
#     print('读打开')
# except NameError as msg:
#
#     print(f'写{msg}')
# except FileNotFoundError as msg:
#     print(f'写{msg}')

# try:
#     # open('test.txt333','r',encoding='utf-8')
#     print(m)
#     # 1/0
#
# except Exception as msg:
#
#     print(f'写1,{msg}')

# try:
#     open('test.txt333','r',encoding='utf-8')
#     print('读打开')
# except Exception as msg:
#
#     print(f'写{msg}')
# else:
#     print('没bug')
# finally:
#     print('我怎么都显示')

# try:
#     print("...........")
#     try:
#         # n=100/0
#         print(n)
#     except NameError as msg:
#         print(f'内层异常{msg}')
# except Exception as msg:
#
#     print(f'写{msg}')

# 抛出异常
# raise NameError('这个变量不存在')


try:
    print("...........")

    try:
        # n=100/0
        print(n)
    except NameError as msg:
        print(f'内层异常{msg}')
        raise
except Exception as msg:

    print(f'写{msg}')
    raise
