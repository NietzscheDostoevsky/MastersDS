def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n == 0:
        return 1# base case
    else:
        return factorial(n -1);
    
def main():
    """Test the factorial function"""
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial not defined for negative numbers")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Enter a valid integer")
