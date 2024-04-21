from sympy import isprime
#metot1
def is_prime(number):
    for i in range (2,number):
        if number % i == 0:
            return False

        else:
            return True




number = int(input("Enter a number: "))

print(is_prime(number))
#metot2

if isprime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
