import sys

try:
    x = int(input("X: "))
    y = int(input("y: "))
except ValueError:
    print(f"Error, invalid input")
    sys.exit(1)

try:
    result = x / y 
except ZeroDivisionError:
    print("Error, can not divide by 0")
    sys.exit(1)
print(f"{x} / {y} = {result}")