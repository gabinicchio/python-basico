"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_inteiro = input('Digite um número inteiro:')

try:
    if (int(numero_inteiro)) % 2 == 0:
        print('Este número é par')
    else:
        print('O número é ímpar')

except:
    print('Não é um número inteiro!')

"""
Forma 1: 
entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Que horas são?')

horas_manha = [0,1,2,3,4,5,6,7,8,9,10,11]
horas_tarde = [12,13,14,15,16,17]
horas_noite = [18,19,20,21,22,23]

if (int(horas)) in horas_manha:
    print('Bom dia!')

elif (int(horas)) in horas_tarde:
    print('Boa tarde!')

else:
    print('Boa noite!')

"""
Forma 2:

entrada = input('Digite a hora em números inteiros:')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >=18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome:')

if (len(nome) <= 4):
    print('Seu nome é curto')

elif (len(nome) == 5) or (len(nome) == 6):
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande!')

"""
Forma 3:

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

"""