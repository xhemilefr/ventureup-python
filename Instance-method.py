	
class Dog:
    species = 'mammal'
	
    def __init__(self, name, age):
	
        self.name = name
        self.age = age
	
    def description(self):
        return "{} is {} years old .".format(self.name, self.age)
	
    def speak(self, sound):
	
        return "{} says {}".format(self.name, sound)

mikey = Dog("Mikey", 6)
bill = Dog("Bill", 4)
	
print(mikey.description())
print(bill.description())
	
print(mikey.speak("Gruff Gruff"))
