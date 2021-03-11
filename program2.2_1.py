def fib(n):
    if n == 1:
        return 1
    elif 1 < n <= 40:
        value_0 = 0
        value_1 = 1
        for i in range(n - 1):
            if i % 2 == 0:
                value_0 += value_1
            else:
                value_1 +=value_0
        return max(value_0,value_1)
            
        
    
    # put your code here

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()