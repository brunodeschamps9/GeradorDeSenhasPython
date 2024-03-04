import random

print('Bem Vindo ao Gerador de Senhas')

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*'

numeros = int(input('Números de senhas para gerar: '))

tamanho = int(input('Tamanho da senha: '))

print('GERADOR DE SENHAS')

for senha in range(numeros):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(letras)
    print(senhas)