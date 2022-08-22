N = int(input())
S = 0
cont=0
numerador = 1

for i in range (N, 0, -1): 
    S = numerador/i
    cont = cont + S 
    numerador = numerador + 1
    if i == 0:
        break

print (cont)