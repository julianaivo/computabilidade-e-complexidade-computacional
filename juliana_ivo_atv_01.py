def soma_klenne(a,b):
    def sucessor(x):
        return x + 1
    resultado = a
    for contador in range(b):
        resultado = sucessor(resultado)

    return resultado

def multiplicacao_kleene (a, b):
    resultado = 0
    for contador in range(b):
        resultado = soma_klenne(resultado, a)
        
    return resultado

#b: base / e: expoente
def potencia_kleene (b, e):
    for contator in range (e):
        resultado_anterior = potencia_kleene (b, e - 1)

        resultado_final = multiplicacao_kleene(b, resultado_anterior)

        return resultado_final
    
    return 1    #caso base: a^0 = 1

print(potencia_kleene(4, 2))  # 16
print(potencia_kleene(5, 2))  # 25
print(potencia_kleene(6, 0))  # 1