# task2_prime_number.py

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


num = int(input("Enter a number between 0 and 1000: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")
