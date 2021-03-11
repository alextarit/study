def fib_digit(n):
    if n == 1:
        return 1
    else:
        value_0 = 0
        value_1 = 1
        for i in range(n - 1):
            if i % 2 == 0:
                value_0 = (value_1 + value_0) % 10
            else:
                value_1 = (value_0 + value_1) % 10
        return value_0 if n % 2 == 0 else value_1 
           


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()