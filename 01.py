def function(n):
    if n == 0:
        return 1
    else:
        return n * function(n-1)
    
n = int(input("Enter a number: "))
print(function(n))
print("The factorial of", n, "is", function(n))

# This program calculates the factorial of a given number using recursion.
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number. ")

