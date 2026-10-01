'''
Matriz
linhas: alfabeto
coluna: estados
'''

matriz = [
    [1, 4, 5, 6, 7, 8, 9, 0, 1, 9],
    [2, 5, 6, 7, 8, 9, 0, 1, 2, 9],
    [3, 6, 7, 8, 9, 0, 1, 2, 3, 0]
]


# w = "1001" #palavra
w = [0, 1, 2] #palavra

# print(matriz[2][4])

estado = 0 #índice do estado inicial

for c in w:
    estado = matriz[c][estado]

print(estado)