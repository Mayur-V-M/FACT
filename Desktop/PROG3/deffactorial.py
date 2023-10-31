def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"The factorial of {number} is {factorial_iterative(number)}")