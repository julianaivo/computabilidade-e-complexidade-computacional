palavra = "(())"

pilha = []  #lista

for char in palavra:

    if char == "(":
        pilha.append("A")

    elif char == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            print("Palavra rejeitada")
            break

else:
    if len(pilha) == 0:
        print("Aceita")
    else:
        print("Rejeitada")