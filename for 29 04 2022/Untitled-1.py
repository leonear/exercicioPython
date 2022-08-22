qnt = int(input())
contador = 0 
soma = 0

for salario in range (1, 1+qnt, 1):

    salario = float(input())

    if salario >= 3000 :
        salario = salario* 1.08 
    elif salario < 3000 and salario >= 2000 :
        salario = salario * 1.10
        contador = contador + 1
    elif salario < 2000 :
        salario = salario * 1.12
    print ( "%.2f" %salario)
    soma += salario 

print (contador)
media = (soma/qnt)
print("%.2f" %media)