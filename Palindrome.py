def is_palindrome(s):
    
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    
    if s == s[::-1]:
        print("Yes, the string is a palindrome.")
    else:
        print("No, the string is not a palindrome.")


test_strings = [
    "A man, a plan, a canal, Panama!",
    "Racecar",
    "hello world",
    "Was it a car or a cat I saw?"
]

for test_string in test_strings:
    print(f"Checking if '{test_string}' is a palindrome:")
    is_palindrome(test_string)
    print()  
