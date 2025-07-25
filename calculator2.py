def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if __name__ == "__main__":
    a = int(input("첫 번째 숫자 입력: "))
    b = int(input("두 번째 숫자 입력: "))
    op = input("연산자 입력 (+, -, *, /): ")

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        if b == 0:
            print("Error: Division by zero.")
            exit()
        result = divide(a, b)
    else:
        print("Invalid operator.")
        exit()

    print("Result:", result)
