# task3_sum_of_squares.py

n = int(input("Enter a positive integer: "))

sum_squares = 0

for i in range(1, n + 1):
    sum_squares += i ** 2

print("Sum of squares from 1 to", n, "=", sum_squares)
