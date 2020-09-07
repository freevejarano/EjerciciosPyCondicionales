def fibonacci(n):
    a=0
    b=1
    c=[]
    aux=0
    while a<n:
        c.append(a)
        aux=a+b
        a=b
        b=aux
    print('Los primeros ',n,' numeros de la serie de fibonacci son:')
    print(c)
    return c

