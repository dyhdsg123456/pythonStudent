class Student(object):

    def __init__(self,name,score):
        self.__name=name
        self.__ore=score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


student = Student('aa', 22)
print(student.get_name())

print(student._Student_name)
