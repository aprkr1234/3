def main():
    try:
        base = float(input("Enter number: "))
        exponent = int(input("Enter exponent: "))
    except ValueError:
        print("Invalid input.")
        return

    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1
    for _ in range(exponent):
        result *= base

    if result.is_integer():
        result = int(result)

    print("Result:", result)

if __name__ == "__main__":
    main()
