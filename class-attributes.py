class Dog:
    #Class Attribute
    species = 'mammal'

    #initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        