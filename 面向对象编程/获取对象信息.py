print(type(123))
print(type('str'))
print(type(None))
print(type(abs))


import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(isinstance((1, 2, 3), (list, tuple)))
print(isinstance([1, 2, 3], (list, tuple)))
print(dir('ABC'))
print(len('acv'))
print('avd'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

class MyProject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

project = MyProject()
print(hasattr(project,'x'))
setattr(project,'y',19)
print(getattr(project,'y'))

print(getattr(project,'z',33))
print(hasattr(project,'power'))
print(getattr(project,'power'))

fn=getattr(project,'power')
print(fn)
print(fn())

def readImg(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None






