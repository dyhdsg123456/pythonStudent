# class Student(object):
#     pass
#
# def set_score(self,score):
#     self.score=score
#
# Student.set_score=set_score

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Abc(object):
    __slots__ = ('name','age')

class GraduateStudent(Abc):
    pass

abc = Abc()
abc.name='11'
abc.age='22'
# abc.score='33'

student = GraduateStudent
student.score=123
