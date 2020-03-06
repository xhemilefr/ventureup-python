	
class Dog:
    species = 'mammal'
	
    def __init__(self, name, age, color):
	
        self.name = name
	
        self.age = age

        self.color = color
	
    def description(self):
        return "{} is {} years old and has {} color".format(self.name, self.age, self.color)
	
    def speak(self, sound):
	
        return "{} says {}".format(self.name, sound)

mikey = Dog("Mikey", 6, "brown")
bill = Dog("Bill", 4, "black")
	
print(mikey.description())
print(bill.description())
	
print(mikey.speak("Gruff Gruff"))
