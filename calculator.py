import math
class calculator:
    result = 0


    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def divide(a, b):
        return a/b

    def squareroot(a):
        return math.sqrt(a)

    def square(a):
        return a*a

    choice = input("Pick a number 1, 2, 3, 4, 5 or 6: ")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1, ' + ', num2, ' = ', addition(num1, num2))

    if choice == '2':
        print(num1, ' - ', num2, ' = ', subtraction(num1, num2))

    if choice == '3':
        print(num1, ' * ', num2, ' = ', multiplication(num1, num2))

    if choice == '4':
        print(num1, ' / ', num2, ' = ', divide(num1, num2))

    if choice == '5':
        print('squareroot ', num1, ' = ', squareroot(num1))

    if choice == '6':
        print(num1, ' * ', num1, ' = ', square(num1))
