class Student(object):

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer')
        if value<0 or value>100:
            raise ValueError('score must 1-100')
        self._score=value

student = Student()
student.score=60
print(student.score)

class Sss(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


sss = Sss()
sss.age='123'
