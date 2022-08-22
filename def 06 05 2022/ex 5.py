def funcao1 ():
    x = -1 
    while x <= 0 or x > 10: 
        x = int (input ("Número: "))
    return x

def funcao2 (a,b):
    if a > b:
        return b,a
    else:
        return a,b

n1 = funcao1()
n2 = funcao1()
(p1,p2) = funcao2 (n1,n2)
print (p1, "e", p2)

