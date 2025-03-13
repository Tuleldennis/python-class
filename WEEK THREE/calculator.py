def calculator_function(num1, num2, operation):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Invalid operation"

    return f"{num1} {operation} {num2} = {result}"


def main():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        result = calculator_function(num1, num2, operation)
        print(result)

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    main()
