def check_palindrome(s):
    return s.lower() == ''.join(reversed(s.lower()))
print(check_palindrome("Talat"))