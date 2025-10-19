import sys

def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts the second number from the first."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divides the first number by the second. Handles division by zero."""
    # Prevent division by zero
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

# Map operators to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate():
    """Main function to run the console calculator."""
    print("Welcome to the Basic Python Calculator!")
    print("Available operations: +, -, *, /")
    print("Type 'exit' to quit the calculator at any time.\n")

    while True:
        try:
            # 1. Get first number
            num1_input = input("Enter first number (or 'exit'): ").strip().lower()
            if num1_input == 'exit':
                print("Exiting calculator. Goodbye!")
                sys.exit()

            # Attempt to convert input to a float
            num1 = float(num1_input)

            # 2. Get operation
            operator = input("Enter operation (+, -, *, /): ").strip()
            if operator == 'exit':
                print("Exiting calculator. Goodbye!")
                sys.exit()

            if operator not in operations:
                print("Invalid operator. Please use one of: +, -, *, /")
                continue

            # 3. Get second number
            num2_input = input("Enter second number: ").strip().lower()
            if num2_input == 'exit':
                print("Exiting calculator. Goodbye!")
                sys.exit()

            num2 = float(num2_input)

            # 4. Perform calculation
            calculation_function = operations[operator]
            result = calculation_function(num1, num2)

            # 5. Display result
            print(f"\n{num1} {operator} {num2} = {result}\n")

        except ValueError:
            # Catches errors if the user enters non-numeric text (like 'hello')
            print("\nInvalid input. Please ensure you enter valid numbers.\n")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}\n")

if __name__ == "__main__":
    calculate()
