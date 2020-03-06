list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def separate_even_from_odd(numbers):
    even_list=[]
    odd_list=[]
    for num in numbers:
        if num % 2==0:
            even_list.append(num)
            
        else:
            odd_list.append(num)
    return {"Odd list": odd_list, "even_list": even_list}
print(separate_even_from_odd(list1))
