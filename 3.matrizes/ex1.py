# 1- Declare uma matriz 10 x 10 e escreva a localização (linha e a coluna) do maior valor.

matriz = []
maior = 0

for i in range(10):
    matriz.append([])
    for j in range(10):
        matriz[i].append(int(input(f'Digite o valor da posição [{i+1}, {j+1}]: ')))
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j

print(f'\nO maior valor é {maior} e está na posição [{linha+1}, {coluna+1}]')
