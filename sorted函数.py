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
    def sun():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f=lazy_sum(1,2,3,4)
print(f)
print(f(1,2,3,4))
# print(f())