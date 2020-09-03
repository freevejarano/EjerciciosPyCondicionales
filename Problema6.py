
def palindroma(palabra):
    a=list(palabra)
    b=[]
    i=len(a)
    j=0

    while i>=0:
        b[i]=b[j]
        i-=1
        i+=1

    return a


