def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def calculate_expression(expr):
    parts = expr.strip().split()

    if len(parts) != 3:
        print("Invalid input.")
        return

    a_str, op, b_str = parts

    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        print("Invalid number.")
        return

    if op == '+':
        result = add(a, b)
    el
