class Student(object):
    def __init__(self, name):
      self.name = name
    def __str__(self):
        return 'Student object (name: %s)'%self.name

print(Student('Michael'))
s = Student('Michael')
print(s)


class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 # 初始化两个计数器a，b

    def __iter__(self):
        return self# 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>200: # 退出循环的条件
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    # def __getattr__(self, item):
    #     if item=='score':
    #         return 99

    def __getattr__(self, item):
        if item == 'age':
           return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)



student = Student()
print(student.name)
# print(student.score)
print(student.age())


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

        __repr__ = __str__

print(Chain().status.user.timeline.list)

class Student2(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s.'%self.name)

s=Student2('aa')
s()

# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(callable(Student()))
print(callable(max))
print(callable(Student2('1')))