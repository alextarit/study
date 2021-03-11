def fib_mod(n, m):
    list_find = []
    list_find.append(0)
    list_find.append(1)
    if n == 1:
        return list_find[n % len(list_find)]
    n_0 = 0
    n_1 = 1
    for i in range(m * 6):
        n_9, n_1 = n_1, (n_0 + n_1) % m
        list_find.append(n_1 % m)
        if list_find[len(list_find) - 1] == 1 and list_find[len(list_find) - 2] == 0:
            break
    return list_find[n % len(list_find)]

def fib_mod(n, m):
    n_0 = 0
    n_1 = 1 
    quantity = 0
    indicator = True
    while n_0 != 0 or (n_0 + n_1) % m != 1 or indicator:
        n_0, n_1 = n_1, (n_0 + n_1) % m
        quantity += 1
        indicator = False    
    n_0 = 0
    n_1 = 1
    n %= quantity
    if n == 0:
        return 0
    elif n == 1:
        return 1
    n -= 1
    for i in range(n):
        if i % 2 == 0:
            n_0 += n_1
        else:
            n_1 += n_0
    return max([n_1, n_0]) % m
    

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()