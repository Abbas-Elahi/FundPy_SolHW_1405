count = 0

while True:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    op = input("Operator (+, -, *, /, **): ")

    result = None

    if op == "+":
        result = a + b

    elif op == "-":
        result = a - b

    elif op == "*":
        result = a * b

    elif op == "/":
        if b == 0:
            print("Cannot divide by zero!")
        else:
            result = a / b

    elif op == "**":
        result = a**b

    else:
        print("Invalid operator!")

    if result is not None:
        print("Result:", result)
        count += 1

    again = input("Continue? (y/n): ")

    if again == "n":
        break

print("Goodbye!")
print("Total calculations:", count)
