def remove_even(numbers):
    counter = 0
    for num in numbers:
        if num % 2 == 0:
            counter += 1
    return counter 
list1 = [10, 21, 4, 45, 66, 92]
print(remove_even(list1))
