def area_triangulo (base,alt):
    area = (base*alt) /2
    return area

def entrada (texto):
    n = int (input(texto))
    return n 

def main ():
    base = entrada ("Digite a base:")
    altura = entrada ("Digite a altura:")
    area = area_triangulo (base, altura)
    print ("Área do trabalho: ", area)

main ()