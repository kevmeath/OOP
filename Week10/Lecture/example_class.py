class Student(object):
    def __init__(self, first='', last='', id=0):
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id

    def __str__(self):
        return '{} {}, ID: {}'.format(self.first_name_str, self.last_name_str, self.id_int)


student1 = Student("Kevin", "Meath", 123456)
print(student1)
