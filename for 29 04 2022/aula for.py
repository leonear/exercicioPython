soma = 0

for dia in range (1,31,1):
    qtd = int(input("Entre com a quantidade do dia %d: " %dia))
    soma = soma + qtd 

media = soma/30
print ("Média= %.2f" %media)