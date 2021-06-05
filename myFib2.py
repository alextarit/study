# Алгоритмы и структуры данных шаг 2.2 задача 2

def fib_digit(n):
    value = 0
    value1 = 1
    if n == 1:
        return 1
    n -= 1
    for i in range(n):
        if i % 2 == 0:
            value = (value + value1) % 10
        else:
            value1 = (value + value1) % 10
    return value1 if n % 2 == 0 else value


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
