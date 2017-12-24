# coding=utf-8


class Person(object):
    count = 0
    address = 'earth'

    __slots__ = ('name', 'gender', 'birth', '__score')

    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__score = 100
        Person.count += 1

    def get_score(self):
        return self.__score

    def who_am_i(self):
        print 'i am a person, my name is: ', self.name

    @classmethod
    def get_count(cls):
        return cls.count


class Student(Person):
    def __init__(self, name, gender, birth, school, score):
        super(Student,self).__init__(name, gender, birth)
        self.school = school
        self.score = score

    def who_am_i(self):
        print 'i am a student, my name is: ', self.name

    def __str__(self):
        return 'student: %s, %s' %(self.school, self.score)

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    def __call__(self, grade):
        print 'i am a student, name is: ', self.name
        print 'grade is: ', grade


class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a


class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'


class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'


class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'


if __name__ == '__main__':
    xiaoming = Person('xiaoming', 'female', '1999')
    print Person.count
    xiaohong = Person('xiaohong', 'male', '2000')
    print Person.count
    print xiaoming.get_count()

    print xiaoming.birth
    print xiaohong.birth

    print Person.address
    print xiaohong.address
    Person.address = 'mars'
    print Person.address
    print xiaoming.address

    print xiaoming.get_score()

    stu_wang = Student('wang', 'male', '2000', 'nanjing', 99)
    print stu_wang.name
    print stu_wang.score

    print isinstance(stu_wang, Person)
    print isinstance(xiaoming, Student)

    print stu_wang.who_am_i()
    print xiaoming.who_am_i()

    d_object = D('d_object')

    print dir(stu_wang)
    print getattr(stu_wang, 'name')
    setattr(stu_wang, 'name', 'wang1')
    print getattr(stu_wang, 'name')

    print stu_wang

    stu_wang.score = 12
    print stu_wang.score

    stu_wang('3')



