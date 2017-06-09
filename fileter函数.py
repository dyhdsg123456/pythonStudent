#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# def is_odd(n):
#     return n%2 ==1

# print(list(filter(is_odd,[1,2,3,5,32,12,11])))

# def not_empty(s):
#     return s and s.strip()
#
# print(list(filter(not_empty,['a','','b'])))
# 用filter求素数
# def _odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# def primes():
#     yield 2
#     it=_odd_iter()#初始序列
#     while True:
#         n=next(it)#返回序列的第一个数
#         yield n
#         it=filter(_not_divisible(n),it)
#
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

        # 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()
        # 滤掉非回数：

# def is_palindrome(n):
#     return n>=1 and str(n)==str(n)[::-1]
#
# output = filter(is_palindrome, range(1, 1000))
# print(list(output))



