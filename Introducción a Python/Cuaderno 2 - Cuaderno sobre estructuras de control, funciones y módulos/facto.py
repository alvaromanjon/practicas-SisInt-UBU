# módulo para calcular el factorial

def factorial(n):
    '''
    Calcula el factorial de un número (versión iterativa).
    
    Parameters
    ----------
    n : número
        entero del que se desea calcular el factorial
       
    Returns
    -------
    int : factorial del número que se le ha pasado
    '''
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def factorial_rec(n):
    '''
    Calcula el factorial de un número (versión recursiva).
    
    Parameters
    ----------
    n : número
        entero del que se desea calcular el factorial
       
    Returns
    -------
    int : factorial del número que se le ha pasado
    '''
    if n > 1:
        return n * factorial_rec(n-1)
    
    return 1

if __name__ == "__main__":
    import sys
    print(factorial(int(sys.argv[1])))

