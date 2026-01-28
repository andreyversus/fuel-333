def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def main():
    print("Simple Python Calculator")
    print("Available operations: +  -  *  /")

    try:
        operation = input("Operation: ").strip()
        a = float(input("First number: "))
        b = float(input("Second number: "))

        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            print("Unknown operation")
            return

        print("Result:", result)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()