class Person:
    def __init__(self, name, surname, birthdate, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
class student(Person):
    def id(self, student_id)
        return "{} student id is {}".format(self.name, student_id)
    def average(self, grade_average)
        return "{} grade average is {}".format(self.name, grade_average)
class staff(Person):
    def id(self, auth_id)
        return "{}{}".format(self.name, auth_id)
    