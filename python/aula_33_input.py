#nome = input('Informe seu nome completo: ')
#print(f'Seja bem vindo {nome}')

#Dessa forma é feito apenas umas concatenação, pois são strings
#numero_1 = input('Digite um número: ')
#numero_2 = input('Digite um outro número: ')

#Dessa forma da certo em parte, pois pode quebrar o sistema se o usuário digitar uma letra por exemplo
#não tem como verificar o que foi adicionado pois quebra no inicio
#numero_1 = int(input('Digite um número: '))
#numero_2 = int(input('Digite um outro número: '))

#Essa forma abaixo é a mais ideal, o codigo fica um pouco maisor mas fica organizado e é uma boa prática
numero_1 = input('Digite um número: ')
numero_2 = input('Digite um outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)


print(f'A soma dos número é: {int_numero_1 + int_numero_2}')

