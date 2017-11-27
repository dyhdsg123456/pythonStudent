# def abc():
#     print('2012')
#
# f=abc
#
# print(abc.__name__)
# print(f.__name__)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

print(now())

