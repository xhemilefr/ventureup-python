def even_number(a):
    b = 0
    for x in a:
        if x % 2 == 0:
            b += 1
    return b

def even_list(a):
    for b in a:
        if b % 2 == 0:
            print(b, end = ",") 

def odd_number(a):
    b = 0 
    for x in a:
        if x % 2 != 0:
            b += 1
    return b

def odd_list(a):
    for b in a:
        if b % 2 != 0:
            print(b, end = ",") 


print("Type the items you want in your list (only numbers), by pressing space: ")
x = [int(x) for x in input().split()]
print("Your list is = ", x)
print("Your list have ", even_number(x), " even numbers")
print("Your list have ", odd_number(x), " odd numbers")
print(even_list(x),"List of even numbers") 
print(odd_list(x), "List of odd numbers")


input("Press enter to close")