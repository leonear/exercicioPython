qtd = int(input())
cont10 = 0
soma = 0 


for sal in range (1, 1+qtd, 1):
    sal= float(input())
    if (sal < 2000):
        sal = sal * 1.12
      
    elif (sal >= 2000 and sal < 3000):
        sal = sal * 1.1
        cont10 = cont10 + 1 
       
    else:
        sal = sal * 1.08
    
    print ("%.2f" %sal)
    soma += sal  


print (cont10)
media = (soma/qtd)
print ("%.2f" %media)
