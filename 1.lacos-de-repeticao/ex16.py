'''16- Faça um programa que receba a idade, altura e o peso de 25 pessoas, Calcule e mostre:

A quantidade de pessoas com idade superior a 50 anos;
A média das Alturas das pessoas com idade entre 10 e 20 anos
A porcentagem das pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.
'''

idade = []  # Lista para armazenar as idades            
altura = []  # Lista para armazenar as alturas
peso = []  # Lista para armazenar os pesos

for i in range(25):  # Loop para receber os dados
    idade.append(int(input(f'Digite a idade da {i+1}ª pessoa: ')))
    altura.append(float(input(f'Digite a altura da {i+1}ª pessoa: ')))
    peso.append(float(input(f'Digite o peso da {i+1}ª pessoa: ')))

# Variáveis para armazenar os resultados
maior50 = 0
media = 0
menor40 = 0

for i in range(25):  # Loop para analisar os dados
    if idade[i] > 50:  # Se a idade for maior que 50
        maior50 += 1  # Adiciona 1 a variável maior50
        
    if idade[i] >= 10 and idade[i] <= 20:  # Se a idade estiver entre 10 e 20
        media += altura[i]  # Adiciona a altura a variável media
        
    if peso[i] < 40:  # Se o peso for menor que 40
        menor40 += 1  # Adiciona 1 a variável menor40
    
media /= 25  # Calcula a média
porcentagem = (menor40 / 25) * 100  # Calcula a porcentagem

# Imprime os resultados
print(f'\nQuantidade de pessoas com idade superior a 50 anos: {maior50}')
print(f'Média das alturas das pessoas com idade entre 10 e 20 anos: {media:.2f}')
print(f'Porcentagem das pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas: {porcentagem:.2f}%')
      