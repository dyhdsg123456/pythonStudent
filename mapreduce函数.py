
# f=abs
# print(f(-10))
# print(abs(-10))
#
# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-2,-4,abs))

# def f(x):
#     return x*x
#
# r=map(f,[1,2,3])
# print(list(r))

# print(list(map(str,[1,3,12,12])))

# from functools import reduce
# def add(x,y):
#     return x+y
#
# print(reduce(add,[1,2,3,4,5,6]))
#
# def fn(x,y):
#     return x*10+y
#
# print(reduce(fn,[1,3,5,7,9]))
#
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
# print(reduce(fn,map(char2num,'13579')))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

# def normalize(name):
#    return name[0:1].upper()+name[1:].lower()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize,L1))
# print(L2)
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[:1])
from functools import reduce
import math
#
# def prod(L):
#    def pp(x,y):
#        return x*y
#    return reduce(pp,L)
#
# print(prod([1,3,5,7,9]))
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# def str2float(s):
#     def fn(x,y):
#         return x * 10+ y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     s1, s2 = s.split('.', 1)
#     return  reduce(fn,map(char2num,s1+s2))/(math.pow(10,len(s2)))
#
# print('str2float(\'123.456\') =', str2float('123.456'))



