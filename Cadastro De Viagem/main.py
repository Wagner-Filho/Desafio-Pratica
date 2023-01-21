# Fazer um cadastro de viagem (Deve pedir o nome do viajante, 
# dar as opções de destino e imprimir a selecionada)

# Isto importa o objeto viagem_class que está em outro arquivo py 
from viagem_class import viagem_class

# Instanciando o objeto viagem_class
viagem1 = viagem_class('Florida')
viagem2 = viagem_class('Havaí')
viagem3 = viagem_class('Tóquio')
viagem4 = viagem_class('Egito')
viagem5 = viagem_class('Londres')

print('bem vindo(a)! Viagens airport tem algumas ofertas para você!')

# Pede o nome do usuário removendo espaços desnecessários e colocando a primeira letra sempre em maiúscula 
nome = input('Qual é o seu nome? ').strip().title()

print(f'Olá {nome}! É um prazer te conhecer nós temos 5 ofertas para você:' 
# três aspas(''') no python permite quebrar a linha e trabalhar melhor com as impressões 
'''
[1] Florida
[2] Havaí 
[3] Tóquio
[4] Egito
[5] Londres''')

selecao = int(input('Selecione qual viagem você deseja: '))

lista_viagens = [viagem1, viagem2, viagem3, viagem4, viagem5]

# Essa variável faz com que a seleção do usuário esteja de acordo com 
# O index da list uma vez que o index começa em 0 
selecao_user = selecao - 1

# Verificação para ver se o user digitou um número valido de 1 a 5
while selecao >= 6:
    print(f'Ops, parece que você digitou uma opção que não existe')

    selecao = int(input('Selecione uma opção de 1 a 5: '))

    # Essa variável faz com que a seleção do usuário esteja de acordo com 
    # O index da list uma vez que o index começa em 0 
    selecao_user = selecao - 1

# Esse if mostra o número que o user digitou e a viagem correspondente a ele atráves do objeto que está referenciado
# Numa lista usando o seu index 
if selecao_user <= 5:
    print(f'A viajem selecionada foi a {selecao}ª opção com destino para {lista_viagens[selecao_user].destino}')


