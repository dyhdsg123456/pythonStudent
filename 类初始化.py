class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

student = Student('aaa', 53)
print(student.name)
print(student.score)
def print_score(std):
    print('%s: %s' % (std.name, std.score))

print_score(student)

student.print_score()
