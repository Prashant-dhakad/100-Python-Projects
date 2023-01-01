#***********************HOW TO BUILD A SIMPLE CALCULATOR In PYTHON STEP BY STEP*******************#
# 1.ADD
# 2.SUBTRACT
# 3.MULTIPLY
# 4.DIVIDE

from typing import final
from unittest import result


print("Select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = int(input("Enter an operaton to perform a task :"))

if operation == 1:
   num1 = int(input("Enter first number :"))
   num2 = int(input("Enter second number :"))
   result = num1 + num2
   print("Addition of first and second number is :", result)
elif operation == 2:
   num1 = int(input("Enter first number :"))
   num2 = int(input("Enter second number :"))
   result = num1 - num2
   print("subtraction of first and second number is :", result)
elif operation == 3:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    result = num1 * num2
    print("Multiplication of first and second number is :", result)
elif operation == 4:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    result = num1 / num2
    print("Divide of first and second number is :", result)
else:
    print("Oops Invalid Operation")