

preco = int(input("Digite o preço do produto:"))
            
nota100= (preco // 100)

if nota100:
    preco = preco % 100
    print ("Notas de 100:", nota100)


nota50 = preco // 50

if nota50:
    preco = preco % 50
    print ("Notas de 50:", nota50)
            

nota20 = preco // 20

if nota20:
    preco = preco % 20
    print ("Notas de 20:", nota20) 
    

nota10 = preco // 10

if nota10:
    preco = preco % 10
    print ("Notas de 10:", nota10)
            

nota5 = preco // 5

if nota5:
    preco = preco % 5
    print ("Notas de 5:", nota5)
            

nota2 = preco // 2

if nota2:
    preco = preco % 2
    print ("Notas de 2:", nota2)
            

nota1 = preco // 1

if nota1:
    preco = preco % 1
    print ("Notas de 1:", nota1)



 
