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
    return c

print(fibonacci(1000))