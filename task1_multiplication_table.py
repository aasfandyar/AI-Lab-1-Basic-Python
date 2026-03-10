# task1_multiplication_table.py

number = int(input("Enter the number: "))
start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

for i in range(start, end + 1):
    result = number * i
    print(f"{number} x {i} = {result}")
