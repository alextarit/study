# Алгоритмы и структуры данных шаг 2.2 задача 1

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        value1 = 1
        value2 = 1
        for i in range(n - 2):
            if i % 2 == 0:
                value1 += value2
            else:
                value2 += value1

        return value1 if value1 > value2 else value2


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
