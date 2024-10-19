def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Invalid input: {e}")
