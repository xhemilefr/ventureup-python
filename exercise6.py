class Dog:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
firstDog = Dog("firstDog", 4)
secondDog = Dog("secondDog", 1)
thirdDog = Dog("thirdDog", 4.5)
def get_biggest_number(*args):
    return max(args)
print("the oldest dog is {} years old.". format(get_biggest_number(firstDog.age, secondDog.age, thirdDog.age)))
# print("{} is {} , {} is {} and {} is {}.".format(
#     firstDog.name, firstDog.age, secondDog.name, secondDog.age, thirdDog.name, thirdDog.age))