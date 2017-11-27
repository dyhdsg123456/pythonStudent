# 按绝对值排序
# print(sorted([-1,1,23,22,12,11-2,-3],key=abs))
# # 字符串忽略大小写排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# # 反向排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# def by_name(t):
#     return t[0]
#
# def by_score(t):
#     return t[1]
#
# L1 = sorted(L, key=by_name)
# L2 = sorted(L, key=by_score)
# print(L1,L2)

# def calc_sum(*args):
#     ax=0
#     for n in args:
#         ax=ax+n
#     return ax
#
# print(calc_sum(1,2,3,4,5,6,7,8))

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
#
# f=lazy_sum(1,2,3,4)
# print(f)
# print(f(1,2,3,4))
# print(f()

# f1=lazy_sum(1,3,5,7,9)
# f2=lazy_sum(1,3,5,7,9)
# print(f1==f2)
#
# def count():
#     fs=[]
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
# f1,f2,f3=count()
#
# print(f1())
# print(f2())
# print(f3())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fx=[]
#     for i in range(1,4):
#         fx.append(f(i))# f(i)立刻被执行，因此i的当前值被传入f()
#     return fx
#
# f1,f2,f3=count()
#
# print(f1())
# print(f2())
# print(f3())

# 一个函数可以返回一个计算结果，也可以返回一个函数。
#
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。