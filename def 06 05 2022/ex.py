valor = float (input())

def atualiza_preco(valor):
    produto = valor * 1.10
    return produto

def taxa(produto):
    taxap = produto * 0.025
    return taxap

def main ():
    produto = atualiza_preco (valor)
    taxap = taxa(produto)
    print ("%.2f" %produto)
    print ("%.2f" %taxap)

main()

