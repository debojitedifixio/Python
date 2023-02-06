# Calculator
# Add
from art import logo
from replit import clear

def add(n1, n2):
    return n1 + n2


# substract
def sub(n1, n2):
    return n1 - n2


# Multiply
def mul(n1, n2):
    return n1 * n2


# divide
def div(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": sub,
              "*": mul,
              "/": div
              }


def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    flag = True
    while flag:
        for symbols in operations:
            print(symbols)
        operations_symbol = input("Select a operation symbol: ")

        num2 = float(input("Enter the next number: "))

        answer = operations[operations_symbol](num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice = input(
            f"If you want to continue with previous result {answer} press 'Y' else press 'N' to start a new "
            f"calculation and type any to exit. ").lower()

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            flag = False
            clear()
            calculator()
        else:
            flag = False
            print(f"Final Result : {answer}")


calculator()
