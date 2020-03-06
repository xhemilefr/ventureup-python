class Person:
    nationality = 'albanian'
    def __init__(self, first_name, last_name, birthdate, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.email = email
    def description(self):
        return "{} {} is born in {} and his email is {}". format(self.first_name, self.last_name, self.birthdate, self.email)
    def habits(self, eat, sleep, walk):
        return "{} likes to eat at {}, sleeps at {} and walks at {}". format(self.first_name,eat, sleep, walk)
        
Enes = Person("Enes", "Shala", 1997, "enesishala@gmail.com")
print(Enes.description())
print(Enes.habits("7 a.m"," 11 p.m"," 6 a.m"))


# postgres sql 