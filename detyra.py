class Person:
    def __init__(self, name, surname, birthdate, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
    def description(self):
        return " Name:{}, Surname: {}, birthdate: {}, email: {}".format(self.name, self.surname, self.birthdate, self.email)
class Student(Person):
    def __init__(self, name, surname, birthdate, email, student_id, grade_average):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
        self.student_id = student_id
        self.grade_average = grade_average
    def data(self):
        return " Student Id: {}, Grade average: {}".format(self.student_id, self.grade_average)
class Staff(Person):
    def __init__(self, name, surname, birthdate, email, auth_id, role, contract_exp_date):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.email = email
        self.auth_id = auth_id
        self.role = role
        self.contract_exp_date = contract_exp_date
    def data(self):
        return " Auth Id: {}, role: {}, Contraxt expiring date: {}".format(self.auth_id, self.role, self.contract_exp_date)
barack = Student("Barack", "Obama", "01.01.1997", "b.obama@gmail.com", "12053110022", "10" )
donald = Staff("Donald", "Trump", "05.12.1968", "d.trump@gmail.com", "123654", "laundryman", "31.01.2020")
print(barack.description())
print(barack.data())
print(donald.description())
print(donald.data())
print(isinstance(donald, Student))
print(isinstance(barack, Person))
print(isinstance(barack, Staff))
