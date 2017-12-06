# from hello import Hello
# h=Hello()
# h.hello()
# print(type(Hello))
# print(type(h))
#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello

#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

def fn(self,name='world'):
    print('Hello, %s.' % name)

# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello =type('Hello',(object,),dict(hello=fn)) #创建Hello class
h=Hello()
h.hello()