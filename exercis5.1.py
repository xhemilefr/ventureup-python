def reverse_string(string):
    reversed_string = ""
    for x in string:
        reversed_string = x + reversed_string
    return reversed_string

def check_palindrome(string):
    temp = string.lower()
    if temp == reverse_string(temp):
        return True
    return False

print(check_palindrome("Pasddsap"))