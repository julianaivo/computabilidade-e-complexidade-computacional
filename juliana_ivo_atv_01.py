#Função potencia:
# b: base 
# e: expoente

def soma_klenne(a,b):
    def sucessor(x):
        return x + 1
    resultado = a
    for contador in range(b):
        resultado = sucessor(resultado)

    return resultado

def multiplicacao (a, b):
    resultado = 0
    for contador in range(b):
        resultado = soma_klenne(resultado, a)
        
    return resultado

def potencia (b, e):
    for contator in range (e):
        resultado_anterior = potencia (b, e - 1)

        resultado_final = multiplicacao(b, resultado_anterior)

        return resultado_final
    
    return 1    #caso base: a^0 = 1

