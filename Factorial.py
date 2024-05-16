def factorial(n):
   
    if n == 0:
        return 1
    
    else:
        return n * factorial(n - 1)


test_numbers = [5, 10, 0, 3]

for num in test_numbers:
    print(f"The factorial of {num} is {factorial(num)}")
