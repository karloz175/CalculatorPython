import math
import myexceptions
from myexceptions import SqrtValueError


def calculate(number1, number2, operation):
    try:
        if operation == "+":
            return number1+number2
        elif operation == "-":
            return number1-number2
        elif operation == "*":
            return number1*number2
        elif operation == "/":
            if number2 == 0:
                raise ZeroDivisionError
            else:
                return number1/number2
        elif operation == "%":
            return number1%number2
        elif operation == "^":
            return pow(number1, number2)
        elif operation == "sqrt":
            return pow(number1, 1/number2)
        else:
            raise ValueError("Wrong value!")
    except ValueError:
        print("Enter the correct value!")
    except ZeroDivisionError:
        print("You can't divide by 0!")

doWeStillCalculate = True
print("Welcome to calculator of 2 numbers:")
print("Possible operations: +, -, /, *, %, sqrt - for sqrt second number is power of sqrt, ^ - for power second number is power)")
while(doWeStillCalculate):
    operation = input("What do you want to do?(insert operation)")
    number1 = float(input("Give first number:"))
    number2 = float(input("Give second number:"))
    result = calculate(number1, number2, operation)


    if result is not None:
        if operation == "sqrt":
            print(str(operation) + "(" + str(number1) + ") = " + str(result) )
        else:
            print(str(number1) + " " + str(operation) + " " + str(number2) + " = " + str(result))
            
    temp = input("Do you want to do another calculation? Type \"no\" if you want to stop program.")
    if temp == "no":
        doWeStillCalculate = False