from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def calculator():
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        operator = input("Enter the operator (+, -, *, /): ")

        if operator == '+':
            result = add(x, y)
        elif operator == '-':
            result = subtract(x, y)
        elif operator == '*':
            result = multiply(x, y)
        elif operator == '/':
            result = divide(x, y)
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            continue

        print(f"The result is: {result}")

        again = input("Do you want to perform another calculation? (Y/N): ").upper()
        if again != 'Y':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()
