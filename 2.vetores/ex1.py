''' 1 - Declare uma lista com 12 posições e em seguida declare também dois valores X e Y quaisquer
correspondentes a duas posições na lista. Ao final seu programa deverá escrever a soma dos valores 
encontrados nas respectivas posições X e Y.'''

lista = []
for i in range(12):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))

x = int(input('Digite a posição X: '))
y = int(input('Digite a posição Y: '))

print(f'A soma dos valores das posições {x} e {y} é {lista[x-1] + lista[y-1]}')
      