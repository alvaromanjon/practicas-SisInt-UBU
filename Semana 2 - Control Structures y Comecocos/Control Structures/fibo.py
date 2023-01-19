# módulo de números Fibonacci

def fib(n):    # escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib_rec(n): # calcula Fibonacci de manera recursiva
    if n <= 2:
        return 1

    return fib_rec(n-1) + fib_rec(n-2)
    
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
