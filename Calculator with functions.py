# Calculator-w-Functions-in-Python
def addition(x, y):
    result = x + y
    print(f"\t{x} + {y} = {result}")


def subtraction(x, y):
    result = x - y
    print(f"\t{x} - {y} = {result}")


def multiplication(x, y):
    result = x + y
    print(f"\t{x} * {y} = {result}")


def division(x, y):
    if y != 0:
        result = x / y
        print(f"\t{x} / {y} = {result}")
    else:
        print("Invalid Option")

while True:
        print("Assignment 1: \nSubmitted by: Christian Travis Dwayne B. Paculba | IT1R10\n")
        x = float(input("Input First Number: "))
        y = float(input("Input Second Number: "))

        print("\n\tChoose an Operator: ")
        print("\t[1] Addition")
        print("\t[2] Subtraction")
        print("\t[3] Multiplication")
        print("\t[4] Division")

        Choice_operator = int(input("\n\tEnter Operator [1-4]: "))

        if Choice_operator == 1:
            addition(x, y)

        elif Choice_operator == 2:
            subtraction(x, y)

        elif Choice_operator == 3:
            multiplication(x, y)

        elif Choice_operator == 4:
            division(x, y)

        Continue = input("Do you want to do another calculation y/n? ")

        if Continue != 'y':
            break
