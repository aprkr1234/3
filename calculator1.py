def basic_calculator():
    print("기본 계산기입니다.")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    choice = input("원하는 연산을 선택하세요 (1/2/3/4): ")

    num1 = float(input("첫 번째 숫자 입력: "))
    num2 = float(input("두 번째 숫자 입력: "))

    if choice == '1':
        print("결과:", num1 + num2)
    elif choice == '2':
        print("결과:", num1 - num2)
    elif choice == '3':
        print("결과:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print("결과:", num1 / num2)
    else:
        print("잘못된 선택입니다.")


def eval_expression():
    print("문자열 수식 계산기입니다.")
    expression = input("계산할 수식을 입력하세요 (예: 2 + 3 * (4 - 1)): ")

    try:
        result = eval(expression)
        print("결과:", result)
    except Exception as e:
        print("오류 발생:", e)


def main():
    print("계산기 프로그램")
    print("1. 기본 사칙연산")
    print("2. 수식 입력 계산")
    mode = input("모드를 선택하세요 (1/2): ")

    if mode == '1':
        basic_calculator()
    elif mode == '2':
        eval_expression()
    else:
        print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
