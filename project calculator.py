print("Calculator")
import math
num = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print("num added to num2 = " + str(num + num2))
print("num subtracted from num2 = " + str(num - num2))
print("num multiplied by num2 = " + str(num * num2))
try:
    print("num divided by num2 = " + str(num / num2))
except ZeroDivisionError:
    print("Cannot divide by zero.")

