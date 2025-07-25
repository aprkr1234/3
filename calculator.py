def add(a, b):
    """덧셈 함수"""
    return a + b

def subtract(a, b):
    """뺄셈 함수 (a - b)"""
    return a - b

def multiply(a, b):
    """곱셈 함수"""
    return a * b

def divide(a, b):
    """나눗셈 함수 (a / b)"""
    if b == 0:
        return "Error: Division by zero."
    return a / b

def basic_calculator():
    """기본 계산기 모드"""
    print("=== 기본 계산기 모드 ===")
    
    try:
        # 사용자 입력 받기
        num1 = int(input("첫 번째 숫자를 입력하세요: "))
        operator = input("연산자를 입력하세요 (+, -, *, /): ")
        num2 = int(input("두 번째 숫자를 입력하세요: "))
        
        # 연산 수행 (하나의 연산자만 처리)
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            # 이 부분은 위에서 이미 체크했지만 안전장치
            print("Invalid operator.")
            return
        
        # 결과 출력
        if isinstance(result, str):  # 에러 메시지인 경우
            print(result)
        else:
            print(f"Result: {result}")
            
    except ValueError:
        print("잘못된 숫자 입력입니다.")

def expression_calculator():
    """문자열 수식 입력 방식 계산기 (연산자 하나만 허용)"""
    print("=== 수식 입력 계산기 모드 ===")
    print("형식: '숫자 연산자 숫자' (예: 2 + 3)")
    
    try:
        expression = input("Enter expression: ")
        
        # 수식을 공백으로 분리
        parts = expression.split()
        
        # 정확히 3개 부분이어야 함 (숫자 연산자 숫자)
        if len(parts) != 3:
            print("잘못된 입력 형식입니다. '숫자 연산자 숫자' 형태로 입력하세요.")
            return
        
        # 숫자와 연산자 추출
        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
        except ValueError:
            print("잘못된 숫자 형식입니다.")
            return
        
        # 연산자가 하나인지 확인 (허용된 연산자만)
        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator.")
            return
        
        # 연산 수행
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator.")
            return
        
        # 결과 출력
        if isinstance(result, str):  # 에러 메시지인 경우
            print(result)
        else:
            print(f"Result: {result}")
            
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    print("반달곰 커피 매장 계산기")
    print("1. 기본 계산기")
    print("2. 수식 입력 계산기")
    
    try:
        choice = input("모드를 선택하세요 (1 또는 2): ")
        
        if choice == '1':
            basic_calculator()
        elif choice == '2':
            expression_calculator()
        else:
            print("잘못된 선택입니다. 1 또는 2를 입력하세요.")
    
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")