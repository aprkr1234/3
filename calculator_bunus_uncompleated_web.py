def evaluate_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        expr = input("계산식을 입력하세요 (예: 2 + 3 * 4): ")
        if expr.lower() in ['exit', 'quit']:
            break
        print("결과:", evaluate_expression(expr))
