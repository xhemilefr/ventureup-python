class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
firstDog = Dog("firstDog", 5)
secondDog = Dog("secondDog", 2)
thirdDog = Dog("thirdDog", 7)
def get_biggest_number(*args):
    return max(args)
print("the oldest dog is {} years old.". format(get_biggest_number(firstDog.age, secondDog.age, thirdDog.age)))