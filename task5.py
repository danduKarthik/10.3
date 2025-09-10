def div(a, b):
    try: return a / b
    except ZeroDivisionError: return "Error: Division by zero"

print(div(float(input("Enter numerator: ")), float(input("Enter denominator: "))))
